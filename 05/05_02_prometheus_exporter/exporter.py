import re
import time

import prometheus_client as prom_client
from prometheus_client import core as prom_core


BIND_PORT = 8000


class DDStatusCollector(object):

    @staticmethod
    def collect():
        with open("/status.txt", "r") as f:
            data = f.read()

        last_string = data.strip().split("\n")[-1]
        re_search = re.search(r"\((\d+)\sMB\)", last_string)
        if not re_search:
            raise Exception("Bad status file!")

        mb = re_search.group(1)

        metric = prom_core.GaugeMetricFamily("DD", "help text (not very)",
                                             value=mb)
        yield metric


if __name__ == "__main__":
    prom_client.start_http_server(BIND_PORT)
    prom_core.REGISTRY.register(DDStatusCollector())
    while True:
        time.sleep(1)
