import random
import json
import time
from datetime import datetime
from pathlib import Path


DATA_FILE = Path("iot/sensor_data.json")


def generate_sensor_data():

    temperature = round(random.uniform(25, 95), 2)
    humidity = round(random.uniform(30, 90), 2)
    vibration = round(random.uniform(0, 10), 2)
    voltage = round(random.uniform(210, 250), 2)
    current = round(random.uniform(1, 10), 2)

    if temperature > 80 or vibration > 8:
        status = "CRITICAL"
    elif temperature > 70 or vibration > 6:
        status = "WARNING"
    else:
        status = "NORMAL"

    return {
        "timestamp": datetime.now().isoformat(),
        "temperature": temperature,
        "humidity": humidity,
        "vibration": vibration,
        "voltage": voltage,
        "current": current,
        "status": status
    }


def save_sensor_data(data):

    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    existing_data = []

    if DATA_FILE.exists():
        try:
            existing_data = json.loads(DATA_FILE.read_text())
        except json.JSONDecodeError:
            existing_data = []

    existing_data.append(data)

    DATA_FILE.write_text(
        json.dumps(existing_data, indent=2)
    )


if __name__ == "__main__":

    print("===== IoT SENSOR SIMULATOR =====")

    for i in range(10):

        sensor_data = generate_sensor_data()

        print(json.dumps(sensor_data, indent=2))

        save_sensor_data(sensor_data)

        time.sleep(2)

    print("\nSensor data saved to:")
    print(DATA_FILE)