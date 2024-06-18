# output_formatter.py

def format_human_readable(results):
    formatted_results = []
    total_requests = 0
    total_time = 0
    total_success = 0
    total_errors = 0
    total_words = 0

    for result in results:
        question = result["question"]
        performance = result["performance"]

        question_str = f"Model: {question['model']}\nPrompt: {question['prompt']}\nMax Tokens: {question['max_tokens']}\nTemperature: {question['temperature']}"
        performance_str = "\n".join([(
            f"Endpoint: {endpoint}\n"
            f"Total Requests: {metrics['total_requests']}\n"
            f"Total Time: {metrics['total_time']:.2f} seconds\n"
            f"Average Response Time: {metrics['average_response_time']:.2f} seconds\n"
            f"Average Words: {metrics['average_words']:.2f}\n"
            f"Success Count: {metrics['success_count']}\n"
            f"Error Count: {metrics['error_count']}\n"
            f"Errors: {metrics['errors']}\n"
        ) for endpoint, metrics in performance.items()])

        formatted_results.append(f"Question:\n{question_str}\nPerformance:\n{performance_str}\n")

        for endpoint, metrics in performance.items():
            total_requests += metrics['total_requests']
            total_time += metrics['total_time']
            total_success += metrics['success_count']
            total_errors += metrics['error_count']
            total_words += metrics['total_words']

    summary = (
        f"Summary:\n"
        f"Total Requests: {total_requests}\n"
        f"Total Time: {total_time:.2f} seconds\n"
        f"Average Response Time: {total_time / total_requests:.2f} seconds\n"
        f"Total Success: {total_success}\n"
        f"Total Errors: {total_errors}\n"
        f"Total Words: {total_words}\n"
        f"Average Words: {total_words / total_requests:.2f}\n"
    )

    return "\n".join(formatted_results) + "\n" + summary
