# output_formatter.py

def format_human_readable(results):
    formatted_results = []
    for result in results:
        question = result["question"]
        performance = result["performance"]

        question_str = f"Model: {question['model']}\nPrompt: {question['prompt']}\nMax Tokens: {question['max_tokens']}\nTemperature: {question['temperature']}"
        performance_str = (f"Total Requests: {performance['total_requests']}\n"
                           f"Total Time: {performance['total_time']:.2f} seconds\n"
                           f"Average Response Time: {performance['average_response_time']:.2f} seconds\n"
                           f"Success Count: {performance['success_count']}\n"
                           f"Error Count: {performance['error_count']}")

        formatted_results.append(f"Question:\n{question_str}\nPerformance:\n{performance_str}\n")
    return "\n".join(formatted_results)
