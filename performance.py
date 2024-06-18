# performance.py
def measure_performance(results):
    total_time = sum(result['response_time'] for result in results)
    success_count = sum(1 for result in results if result['status_code'] == 200)
    error_count = len(results) - success_count

    return {
        "total_requests": len(results),
        "total_time": total_time,
        "average_response_time": total_time / len(results),
        "success_count": success_count,
        "error_count": error_count
    }
