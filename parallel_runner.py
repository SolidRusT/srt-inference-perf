# parallel_runner.py
from concurrent.futures import ThreadPoolExecutor
from api_client import query_vllm

def run_tests_in_parallel(endpoints, payload, num_threads=4):
    results = []
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(query_vllm, endpoint, payload) for endpoint in endpoints]
        for future in futures:
            results.append(future.result())
    return results
