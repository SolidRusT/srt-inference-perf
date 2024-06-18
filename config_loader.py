# config_loader.py
import yaml
import json

def load_config(file_path):
    with open(file_path, 'r') as file:
        if file_path.endswith('.yaml') or file_path.endswith('.yml'):
            return yaml.safe_load(file)
        elif file_path.endswith('.json'):
            return json.load(file)
        else:
            raise ValueError("Unsupported file format. Use .yaml, .yml, or .json")

# Example usage
config = load_config('config.yaml')
