#!/usr/bin/env python

import socket
import time

import psutil

MEASUREMENT_NAME = "MEM"


def _get_tags():
    tags_data = [
        ("hostname", socket.gethostname())
    ]
    tags = ",".join("=".join(item) for item in tags_data)
    return tags


def _get_mem_usage():
    virtual_memory = psutil.virtual_memory()
    mem_usage = {
        "py_total": virtual_memory.total,
        "py_available": virtual_memory.available,
        "py_percent": virtual_memory.percent,
        "py_used": virtual_memory.used,
        "py_free": virtual_memory.free,
    }
    return mem_usage


def _get_metrics():
    mem_usage = _get_mem_usage()
    metrics = ",".join("=".join(map(str, item))
                       for item in mem_usage.items())
    return metrics


def _get_output():
    tags = _get_tags()
    metrics = _get_metrics()
    timestamp = int(time.time() * (10 ** 9))

    output = f"{MEASUREMENT_NAME},{tags} {metrics} {timestamp}"
    return output


if __name__ == "__main__":
    output = _get_output()
    print(output)
