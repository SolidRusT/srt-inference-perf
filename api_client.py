# api_client.py
import requests
import time

def query_vllm(endpoint, payload):
    headers = {"Content-Type": "application/json"}
    start_time = time.time()
    try:
        response = requests.post(endpoint, json=payload, headers=headers)
        response.raise_for_status()
        end_time = time.time()
        content = response.json()
        word_count = len(content.get("choices", [{}])[0].get("text", "").split())
        return {
            "response_time": end_time - start_time,
            "status_code": response.status_code,
            "content": content,
            "word_count": word_count
        }
    except requests.exceptions.RequestException as e:
        end_time = time.time()
        return {
            "response_time": end_time - start_time,
            "status_code": None,
            "error": str(e),
            "error_details": e.response.text if e.response else str(e)
        }
