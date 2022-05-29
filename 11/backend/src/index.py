import asyncio
import signal
import sys
import uuid
from datetime import datetime

import tornado.gen
import tornado.httpserver
import tornado.ioloop
import tornado.log
import tornado.options
import tornado.web


tornado.options.define("port", default=8888, type=int)

GRACEFUL_SHUTDOWN_CAP_TIMEOUT = 20  # seconds
GRACEFUL_SHUTDOWN_STEP_TIMEOUT = 5  # seconds

LOG = tornado.log.gen_log


async def heavy_task():
    res = datetime.utcnow()
    await asyncio.sleep(13)
    return str(res)


class BaseHandler(tornado.web.RequestHandler):

    def initialize(self):
        self.request_id = uuid.uuid4()  # noqa
        LOG.info("Request %s started", self.request_id)

    async def prepare(self):
        if self.application.is_shutdown_in_progress():
            LOG.warning("Request %s aborted", self.request_id)
            raise tornado.web.HTTPError(503)

        self.application.add_request(self.request_id)

    def on_finish(self):
        self.application.remove_request(self.request_id)
        LOG.info("Request %s finished", self.request_id)


class MainHandler(BaseHandler):

    async def get(self):
        res = await heavy_task()
        self.write({"res": res})


class MyApplication(tornado.web.Application):

    active_requests = set()
    sigterm_dt = None

    def is_shutdown_in_progress(self):
        return bool(self.sigterm_dt)

    def add_request(self, request_id):
        self.active_requests.add(request_id)

    def remove_request(self, request_id):
        self.active_requests.discard(request_id)

    async def graceful_shutdown(self):
        self.sigterm_dt = datetime.utcnow()

        while True:
            if not self.active_requests:
                LOG.info("Graceful shutdown: exiting, no active requests.")
                self.shutdown(exit_code=0)

            delta_sec = (datetime.utcnow() - self.sigterm_dt).total_seconds()
            if delta_sec > GRACEFUL_SHUTDOWN_CAP_TIMEOUT:
                LOG.warning("Graceful shutdown: timeout exceeded, exiting. "
                            "%d active request(s)", len(self.active_requests))
                self.shutdown(exit_code=1)

            LOG.info("Graceful shutdown: waiting, %d active request(s)",
                     len(self.active_requests))

            await asyncio.sleep(GRACEFUL_SHUTDOWN_STEP_TIMEOUT)

    @staticmethod
    def shutdown(exit_code=0):
        tornado.ioloop.IOLoop.instance().stop()
        sys.exit(exit_code)


application = MyApplication([
    (r"/", MainHandler),
])


def shutdown_handler(signum, frame):
    LOG.warning("SIGTERM signal received")
    tornado.ioloop.IOLoop.instance().add_callback_from_signal(
        application.graceful_shutdown)


def main():
    tornado.options.parse_command_line()
    signal.signal(signal.SIGTERM, shutdown_handler)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
