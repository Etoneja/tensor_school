import os
import time

import kubernetes as k8s
import prometheus_client as prom


ENV_APP_PORT = "APP_PORT"
ENV_EXPORTER_PORT = "EXPORTER_PORT"
ENV_POLLING_INTERVAL_SECONDS = "POLLING_INTERVAL_SECONDS"

DEFAULT_APP_PORT = 9080
DEFAULT_EXPORTER_PORT = 9080
DEFAULT_POLLING_INTERVAL = 5  # seconds


class AppMetrics:

    def __init__(self, app_port, polling_interval_seconds):

        self.app_port = app_port
        self.polling_interval_seconds = polling_interval_seconds
        self.k8s_cli = self.get_k8s_cli()
        self.pods_count = prom.Gauge("pods_count", "Pods count")

    @staticmethod
    def get_k8s_cli():
        k8s.config.load_incluster_config()
        return k8s.client.CoreV1Api()

    def run_metrics_loop(self):
        while True:
            self.fetch()
            time.sleep(self.polling_interval_seconds)

    def fetch(self):
        pods = self.k8s_cli.list_pod_for_all_namespaces(watch=False)
        self.pods_count.set(len(pods.items))


def main():
    polling_interval_seconds = int(os.getenv(
        ENV_POLLING_INTERVAL_SECONDS,
        DEFAULT_POLLING_INTERVAL
    ))
    app_port = int(os.getenv(ENV_APP_PORT, DEFAULT_APP_PORT))
    exporter_port = int(os.getenv(ENV_EXPORTER_PORT, DEFAULT_EXPORTER_PORT))

    app_metrics = AppMetrics(app_port, polling_interval_seconds)
    prom.start_http_server(exporter_port)
    app_metrics.run_metrics_loop()


if __name__ == "__main__":
    main()
