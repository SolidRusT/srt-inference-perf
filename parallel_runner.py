# parallel_runner.py
from concurrent.futures import ThreadPoolExecutor, as_completed
from api_client import query_vllm
from tqdm import tqdm
from collections import defaultdict

def run_tests_in_parallel(endpoints, payload, iterations, concurrency, max_parallel_hosts):
    results = []
    progress_bars = {}
    endpoint_progress = defaultdict(lambda: 0)
    futures_to_endpoint = {}

    # Calculate the required number of threads
    num_threads = max_parallel_hosts * concurrency

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Submit all tasks to the executor for all endpoints
        for endpoint in endpoints:
            progress_bars[endpoint] = tqdm(total=iterations * concurrency, desc=f"{endpoint}", unit="request")
            for _ in range(iterations):
                for _ in range(concurrency):
                    future = executor.submit(query_vllm, endpoint, payload)
                    futures_to_endpoint[future] = endpoint

        # Process the futures as they complete
        for future in as_completed(futures_to_endpoint):
            endpoint = futures_to_endpoint[future]
            try:
                result = future.result()
                result["endpoint"] = endpoint
                results.append(result)
            except Exception as e:
                result = {
                    "endpoint": endpoint,
                    "error": str(e)
                }
                results.append(result)
            progress_bars[endpoint].update(1)

    # Close all progress bars
    for bar in progress_bars.values():
        bar.close()

    return results
