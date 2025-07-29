#!/usr/bin/env python3

import json
import subprocess

def parse_sensors_output(data, parent_keys=None):
    if parent_keys is None:
        parent_keys = []

    for key, value in data.items():
        if isinstance(value, dict):
            parse_sensors_output(value, parent_keys + [key])
        elif key.endswith('_input'):
            print(f"{': '.join(parent_keys)}: {value}")

def main():
    try:
        result = subprocess.run(['sensors', '-j'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)
        sensor_data = json.loads(result.stdout)
        parse_sensors_output(sensor_data)
    except FileNotFoundError:
        print("Error: 'sensors' command not found. Please make sure 'lm-sensors' is installed.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing 'sensors' command: {e}")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON output: {e}")

if __name__ == "__main__":
    main()
