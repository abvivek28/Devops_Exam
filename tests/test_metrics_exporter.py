import unittest
from metrics_exporter import get_metrics

class TestMetricsExporter(unittest.TestCase):

    def test_metrics_are_generated(self):
        metrics = get_metrics()

        self.assertIn("demo_requests_total", metrics)
        self.assertIn("demo_cpu_usage_percent", metrics)

    def test_cpu_metric_exists(self):
        metrics = get_metrics()

        self.assertIn("99.9", metrics)

if __name__ == "__main__":
    unittest.main()
