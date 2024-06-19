# parallel_runner.py
from concurrent.futures import ThreadPoolExecutor, as_completed
from api_client import query_vllm
from tqdm import tqdm
from collections import defaultdict
import itertools
import threading
import logging
import psutil
import time

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def log_system_resources():
    cpu_usage = psutil.cpu_percent()
    memory_info = psutil.virtual_memory()
    active_threads = threading.active_count()
    logging.debug(f"Active threads: {active_threads} / Total available threads: {threading.active_count()}")
    logging.debug(f"CPU Usage: {cpu_usage}%")
    logging.debug(f"Memory Usage: {memory_info.percent}%")

def periodic_logging(interval):
    while True:
        log_system_resources()
        time.sleep(interval)

def run_tests_in_parallel(endpoints, payload, iterations, concurrency, thread_multiplier):
    results = []
    progress_bars = {}
    endpoint_progress = defaultdict(lambda: 0)
    futures_to_endpoint = {}

    # Calculate the required number of threads
    num_threads = len(endpoints) * concurrency * thread_multiplier

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Start the periodic logging thread
        logging_thread = threading.Thread(target=periodic_logging, args=(5,))
        logging_thread.daemon = True
        logging_thread.start()

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
