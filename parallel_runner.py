# parallel_runner.py
from concurrent.futures import ThreadPoolExecutor
from api_client import query_vllm

def run_tests_in_parallel(endpoints, payload, num_threads=4):
    results = []
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = {executor.submit(query_vllm, endpoint, payload): endpoint for endpoint in endpoints}
        for future in futures:
            endpoint = futures[future]
            result = future.result()
            result["endpoint"] = endpoint
            results.append(result)
    return results
