# output_formatter.py

def format_human_readable(results):
    formatted_results = []
    for result in results:
        question = result["question"]
        performance = result["performance"]

        question_str = f"Model: {question['model']}\nPrompt: {question['prompt']}\nMax Tokens: {question['max_tokens']}\nTemperature: {question['temperature']}"
        performance_str = "\n".join([(
            f"Endpoint: {endpoint}\n"
            f"Total Requests: {metrics['total_requests']}\n"
            f"Total Time: {metrics['total_time']:.2f} seconds\n"
            f"Average Response Time: {metrics['average_response_time']:.2f} seconds\n"
            f"Success Count: {metrics['success_count']}\n"
            f"Error Count: {metrics['error_count']}\n"
        ) for endpoint, metrics in performance.items()])

        formatted_results.append(f"Question:\n{question_str}\nPerformance:\n{performance_str}\n")
    return "\n".join(formatted_results)
