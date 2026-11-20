from prometheus_client import Counter, Gauge, generate_latest, REGISTRY

REQUESTS = Counter(
    "demo_requests_total",
    "Total number of demo requests"
)

CPU_USAGE = Gauge(
    "demo_cpu_usage_percent",
    "Demo CPU usage percentage"
)

def update_metrics():
    REQUESTS.inc()
    CPU_USAGE.set(45.5)

def get_metrics():
    update_metrics()
    return generate_latest(REGISTRY).decode("utf-8")

if __name__ == "__main__":
    from prometheus_client import start_http_server
    import time

    start_http_server(8000)

    while True:
        update_metrics()
        time.sleep(5)
