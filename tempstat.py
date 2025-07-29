#!/usr/bin/env python3

import json
import subprocess
import time

def get_sensor_readings(data, parent_keys=None, temps=None):
    """Recursively parses sensor data to extract temperature inputs."""
    if parent_keys is None:
        parent_keys = []
    if temps is None:
        temps = {}

    for key, value in data.items():
        if isinstance(value, dict):
            get_sensor_readings(value, parent_keys + [key], temps)
        elif key.endswith('_input'):
            sensor_name = ': '.join(parent_keys)
            temps[sensor_name] = value
    return temps

def main():
    """
    Takes 10 temperature readings every 10 seconds, showing only the values
    that have changed since the last reading.
    """
    previous_temps = {}

    for i in range(10):
        print(f"--- Reading {i + 1}/10 ---")
        try:
            result = subprocess.run(
                ['sensors', '-j'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
                check=True
            )
            sensor_data = json.loads(result.stdout)
            current_temps = get_sensor_readings(sensor_data)

            if i == 0:
                # First reading, compare against 0
                for sensor, temp in current_temps.items():
                    print(f"{sensor}: {temp:.2f} (+{temp:.2f})")
                previous_temps = current_temps
            else:
                # Subsequent readings, compare against previous
                for sensor, temp in current_temps.items():
                    prev_temp = previous_temps.get(sensor, 0.0)
                    if temp != prev_temp:
                        diff = temp - prev_temp
                        sign = '+' if diff > 0 else ''
                        print(f"{sensor}: {temp:.2f} ({sign}{diff:.2f})")
                previous_temps = current_temps

            if i < 9:  # Don't sleep after the final reading
                time.sleep(10)

        except FileNotFoundError:
            print("Error: 'sensors' command not found. Please ensure 'lm-sensors' is installed.")
            break
        except (subprocess.CalledProcessError, json.JSONDecodeError) as e:
            print(f"An error occurred: {e}")
            if i < 9:
                time.sleep(10) # Wait before next attempt

if __name__ == "__main__":
    main()