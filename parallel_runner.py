# parallel_runner.py
from concurrent.futures import ThreadPoolExecutor
from api_client import query_vllm


def run_tests_in_parallel(endpoints, payload, iterations, num_threads=4):
    results = []
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        for _ in range(iterations):
            for endpoint in endpoints:
                futures.append((executor.submit(query_vllm, endpoint, payload), endpoint))

        for future, endpoint in futures:
            result = future.result()
            result["endpoint"] = endpoint
            results.append(result)
    return results
