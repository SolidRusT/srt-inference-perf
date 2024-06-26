# main.py
import argparse
from config_loader import load_config
from parallel_runner import run_tests_in_parallel
from performance import measure_performance
from output_formatter import format_human_readable
from prometheus_exporter import start_prometheus_server

def display_usage():
    return (
        "Usage: python main.py --config CONFIG_PATH [--json] [--usage]\n\n"
        "Arguments:\n"
        "  --config CONFIG_PATH   Path to the configuration file\n"
        "  --json                 Display results in JSON format\n"
        "  --usage                Show this usage message\n"
    )

def main():
    parser = argparse.ArgumentParser(description="srt-inference-perf", add_help=False)
    parser.add_argument("--config", required=False, help="Path to the configuration file")
    parser.add_argument("--json", action="store_true", help="Display results in JSON format")
    parser.add_argument("--usage", action="store_true", help="Show usage message")
    parser.add_argument("--prometheus-port", type=int, help="Port for Prometheus server")

    args, unknown = parser.parse_known_args()

    if args.usage or not args.config or unknown:
        print(display_usage())
        return

    config = load_config(args.config)
    prometheus_port = args.prometheus_port or config.get('prometheus', {}).get('port', 8000)
    start_prometheus_server(prometheus_port)

    questions = config['questions']
    endpoints = config['endpoints']
    iterations = config.get('load_test', {}).get('iterations', 5)
    concurrency = config.get('load_test', {}).get('concurrency', 1)
    thread_multiplier = config.get('load_test', {}).get('thread_multiplier', 7)  # Default to 7 if not specified

    all_results = []
    for question in questions:
        results = run_tests_in_parallel(endpoints, question, iterations, concurrency, thread_multiplier)
        performance = measure_performance(results)
        all_results.append({
            "question": question,
            "performance": performance
        })

    if args.json:
        for result in all_results:
            print(f"Question: {result['question']}")
            print(f"Performance: {result['performance']}")
    else:
        print(format_human_readable(all_results))

if __name__ == "__main__":
    main()
