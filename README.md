# srt-inference-perf

## Overview

`srt-inference-perf` is a powerful tool designed to measure the performance of any OpenAI-compatible completions endpoint, including vLLM, Hugging Face TGI, LLama.CPP Server, and more. This app reads user-defined questions from a JSON or YAML file, queries multiple endpoints, and generates performance metrics for comparison. The primary objective is to help AI teams tune API configuration parameters for optimal performance.

## Features

- Reads questions from a JSON or YAML file
- Queries multiple OpenAI-compatible completions endpoints
- Measures response time, error rate, and other relevant metrics
- Supports parallel testing across multiple endpoints
- Generates a performance report

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/SolidRusT/srt-inference-perf.git
    cd srt-inference-perf
    ```

2. **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. **Copy the example configuration file:**
    ```bash
    cp config-example.yaml config.yaml
    ```

2. **Edit `config.yaml` to suit your needs.**

## Usage

1. **Run the performance tester with your configuration file:**
    ```bash
    python main.py --config config.yaml
    ```

2. **Display the results in a human-readable format:**
    ```bash
    python main.py --config config.yaml --human
    ```

3. **Display the results in JSON format:**
    ```bash
    python main.py --config config.yaml --json
    ```

4. **Show usage instructions:**
    ```bash
    python main.py --usage
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Suparious (suparious@solidrust.net)

## Acknowledgments

This project is developed by SolidRusT Networks.
