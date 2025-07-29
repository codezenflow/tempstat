# tempstat v1.0

`tempstat` is a Python script that monitors your system's temperature sensors. It periodically fetches readings and displays only the values that have changed, making it easy to track temperature fluctuations over time.

## Features

*   **Periodic Monitoring:** Automatically reads sensor data at regular intervals.
*   **Change-Based Reporting:** Only outputs sensor readings that have changed since the last check, reducing noise.
*   **Difference Tracking:** Shows the temperature difference from the previous reading, with a `+` for increases and a `-` for decreases.
*   **Customizable:** Allows you to configure the reading frequency and the total number of readings.

## Requirements

*   Python 3.6+
*   `lm-sensors` installed and configured on your Linux system.

## Usage

To run the script with default settings (5-second interval, 10 readings), simply execute:

```bash
./tempstat.py
```

### Custom Interval and Readings

You can customize the monitoring by providing two optional arguments:

1.  **Interval:** The number of seconds to wait between readings.
2.  **Readings:** The total number of readings to take.

**Example:**

To take 20 readings at a 2-second interval, run:

```bash
./tempstat.py 2 20
```

## Example Output

```
--- Reading 1/10 ---
k10temp-pci-00c3: Tctl: 43.00 (+43.00)

--- Reading 2/10 ---
k10temp-pci-00c3: Tctl: 45.00 (+2.00)

--- Reading 3/10 ---
(No changes)

--- Reading 4/10 ---
k10temp-pci-00c3: Tctl: 44.00 (-1.00)
```