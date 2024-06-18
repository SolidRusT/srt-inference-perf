# main.py
import argparse
from config_loader import load_config
from parallel_runner import run_tests_in_parallel
from performance import measure_performance
from output_formatter import format_human_readable

def main():
    parser = argparse.ArgumentParser(description="vLLM Performance Tester")
    parser.add_argument("--config", required=True, help="Path to the configuration file")
    parser.add_argument("--human", action="store_true", help="Display results in human-readable format")
    args = parser.parse_args()

    config = load_config(args.config)
    questions = config['questions']
    endpoints = config['endpoints']
    iterations = config.get('load_test', {}).get('iterations', 5)

    all_results = []
    for question in questions:
        results = run_tests_in_parallel(endpoints, question, iterations)
        performance = measure_performance(results)
        all_results.append({
            "question": question,
            "performance": performance
        })

    if args.human:
        print(format_human_readable(all_results))
    else:
        for result in all_results:
            print(f"Question: {result['question']}")
            print(f"Performance: {result['performance']}")

if __name__ == "__main__":
    main()
