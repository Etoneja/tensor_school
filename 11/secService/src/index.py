import itertools
import logging
import os
import time

import httpx


TARGET_PROTO = os.environ.get("TARGET_PROTO", "http")
TARGET_HOST = os.environ.get("TARGET_HOST", "127.0.0.1")
TARGET_PORT = os.environ.get("TARGET_PORT", 8888)

TARGET_ENDPOINT = f"{TARGET_PROTO}://{TARGET_HOST}:{TARGET_PORT}/"

SERVICE_MAX_TIMEOUT = 3 * 60  # seconds
SERVICE_DEFAULT_TIMEOUT = 15  # seconds
SERVICE_STEP_TIMEOUT = 5  # seconds

LOG = logging.getLogger(__name__)
formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
LOG.setLevel(logging.DEBUG)
LOG.addHandler(handler)


class Service(object):

    def __init__(self):
        self._timeout = SERVICE_DEFAULT_TIMEOUT

    def _reset_timeout(self):
        if self._timeout != SERVICE_DEFAULT_TIMEOUT:
            LOG.info("Reset timeout from %d to %d",
                     self._timeout, SERVICE_DEFAULT_TIMEOUT)
            self._timeout = SERVICE_DEFAULT_TIMEOUT

    def _increase_timeout(self):
        new_timeout = min(self._timeout * 2, SERVICE_MAX_TIMEOUT)
        if self._timeout != new_timeout:
            LOG.info("Increase timeout from %d up to %d",
                     self._timeout, new_timeout)
            self._timeout = new_timeout

    def _make_request(self):
        try:
            LOG.debug("Performing request to endpoint %s with timeout %d",
                      TARGET_ENDPOINT, self._timeout)
            r = httpx.get(TARGET_ENDPOINT, timeout=self._timeout)
            r.raise_for_status()
            res = r.json()
            LOG.info("Request result: %s", res)
            self._reset_timeout()
            return res

        except Exception as e:
            self._increase_timeout()
            LOG.exception(e)

    def _run(self):
        for i in itertools.count(1):
            LOG.debug("Service step %d", i)
            self._make_request()
            time.sleep(SERVICE_STEP_TIMEOUT)

    def run(self):
        LOG.info("Service started")
        self._run()


def main():
    service = Service()
    service.run()


if __name__ == "__main__":
    main()
