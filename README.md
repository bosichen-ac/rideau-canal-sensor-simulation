# Rideau Canal Sensor Simulation

## Overview

This project simulates IoT sensors that monitor ice conditions on the Rideau Canal Skateway.

It generates real-time telemetry data and sends it to Azure IoT Hub for processing.

## Technologies Used

- Python
- Azure IoT Hub SDK

## Features

- Simulates 3 sensor devices:
  - Dow's Lake
  - Fifth Avenue
  - NAC
- Sends data every 10 seconds
- Generates realistic environmental values

## Prerequisites

- Python 3.13
- Azure IoT Hub instance
- Registered IoT devices (3 devices)

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file from the `.env.example` template:

```env
DOW_S_LAKE=<device-connection-string>
FIFTH_AVENUE=<device-connection-string>
NAC=<device-connection-string>
```

## Usage

Run the simulator:

```bash
python3 sensor_simulator.py
```

The script will continuously send telemetry data to Azure IoT Hub.

## Code Structure

```
rideau-canal-sensor-simulation/
├── README.md                  # Setup and usage instructions
├── sensor_simulator.py        # Main simulation script
├── requirements.txt           # Python dependencies
├── .env.example               # Example environment variables
├── .gitignore
└── config/
    └── sensor_config.json     # Optional: sensor configuration
```

### Key Components

- Data generation function
- Azure IoT Hub client
- Continuous send loop

---

## Sensor Data Format

Example JSON:

```json
{
  "location": "Dow's Lake",
  "iceThickness": 21.79,
  "surfaceTemp": -3.56,
  "snowAccumulation": 1.14,
  "externalTemp": -17.79,
  "timestamp": "2026-04-18T12:00:00Z"
}
```

## Troubleshooting

### No data in IoT Hub

- Check connection string
- Verify device IDs

### Script crashes

- Ensure dependencies are installed
- Check Python version