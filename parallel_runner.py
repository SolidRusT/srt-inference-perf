# parallel_runner.py
from concurrent.futures import ThreadPoolExecutor, as_completed
from api_client import query_vllm
from tqdm import tqdm


def run_tests_in_parallel(endpoints, payload, iterations, concurrency, num_threads=4):
    results = []
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        for _ in range(iterations):
            for endpoint in endpoints:
                for _ in range(concurrency):
                    futures.append((executor.submit(query_vllm, endpoint, payload), endpoint))

        for future, endpoint in tqdm(futures, desc="Testing", unit="request"):
            result = future.result()
            result["endpoint"] = endpoint
            results.append(result)
    return results
