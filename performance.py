# performance.py
from collections import defaultdict

def measure_performance(results):
    endpoint_performance = defaultdict(lambda: {"total_time": 0, "total_requests": 0, "success_count": 0, "error_count": 0, "total_words": 0, "errors": []})

    for result in results:
        endpoint = result["endpoint"]
        endpoint_performance[endpoint]["total_time"] += result["response_time"]
        endpoint_performance[endpoint]["total_requests"] += 1
        endpoint_performance[endpoint]["total_words"] += result.get("word_count", 0)
        if result["status_code"] == 200:
            endpoint_performance[endpoint]["success_count"] += 1
        else:
            endpoint_performance[endpoint]["error_count"] += 1
            endpoint_performance[endpoint]["errors"].append(result.get("error_details", "Unknown error"))

    for endpoint, metrics in endpoint_performance.items():
        metrics["average_response_time"] = metrics["total_time"] / metrics["total_requests"]
        metrics["average_words"] = metrics["total_words"] / metrics["total_requests"]

    return endpoint_performance
