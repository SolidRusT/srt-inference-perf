# parallel_runner.py
from concurrent.futures import ThreadPoolExecutor, as_completed
from api_client import query_vllm
from tqdm import tqdm
from collections import defaultdict
import itertools

def run_tests_in_parallel(endpoints, payload, iterations, concurrency, thread_multiplier):
    results = []
    progress_bars = {}
    endpoint_progress = defaultdict(lambda: 0)
    futures_to_endpoint = {}

    # Calculate the required number of threads
    num_threads = len(endpoints) * concurrency * thread_multiplier

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Create a combined iterable of all tasks for all endpoints
        tasks = list(itertools.chain.from_iterable(
            [(endpoint, query_vllm, payload) for _ in range(iterations) for _ in range(concurrency)]
            for endpoint in endpoints
        ))

        # Submit the tasks to the executor
        futures = {executor.submit(query_vllm, endpoint, payload): endpoint for endpoint, query_vllm, payload in tasks}

        # Create a tqdm progress bar for each endpoint
        for endpoint in endpoints:
            progress_bars[endpoint] = tqdm(total=iterations * concurrency, desc=f"{endpoint}", unit="request")

        # Process the futures as they complete
        for future in as_completed(futures):
            endpoint = futures[future]
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
