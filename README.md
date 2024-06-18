# srt-inference-perf

## Overview

srt-inference-perf is a tool designed to measure the performance of any OpenAI-compatible completions endpoint, including vLLM, Hugging Face TGI, LLama.CPP Server, and more. This app reads user-defined questions from a JSON or YAML file, queries multiple endpoints, and generates performance metrics for comparison. The primary objective is to help AI teams tune API configuration parameters for optimal performance.

## Features

- Reads questions from a JSON or YAML file
- Queries multiple OpenAI-compatible completions endpoints
- Measures response time, error rate, and other relevant metrics
- Supports parallel testing across multiple endpoints
- Generates a performance report

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/SolidRusT/srt-inference-perf.git
    cd srt-inference-perf
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Create a configuration file (`config.yaml` or `config.json`) with your questions and endpoints. Example `config.yaml`:
    ```yaml
    questions:
      - model: "solidrust/Mistral-7B-instruct-v0.3-AWQ"
        prompt: "Role: You are a creative and imaginative storywriter.\nInstruction: Write a simple and engaging poem about who kicked my dog.\nInput:"
        max_tokens: 512
        temperature: 5

    endpoints:
      - http://thanatos:8081/v1/completions
      - http://erebus:8081/v1/completions

    load_test:
      iterations: 5
    ```

## Usage

Run the performance tester with your configuration file:
```bash
python main.py --config config.yaml
```

To display the results in a human-readable format:
```bash
python main.py --config config.yaml --human
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Suparious (suparious@solidrust.net)

## Acknowledgments

This project is developed by SolidRusT Networks.
