# prometheus_exporter.py
from prometheus_client import start_http_server, Summary, Counter, Gauge

# Create Prometheus metrics to track
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
REQUEST_COUNT = Counter('request_count', 'Total number of requests')
SUCCESS_COUNT = Counter('success_count', 'Total number of successful requests')
ERROR_COUNT = Counter('error_count', 'Total number of failed requests')
WORD_COUNT = Summary('word_count', 'Number of words in the response')
CONCURRENCY_LEVEL = Gauge('concurrency_level', 'Number of concurrent requests')

def start_prometheus_server(port=8000):
    start_http_server(port)
