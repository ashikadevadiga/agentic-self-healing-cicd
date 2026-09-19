import json
import random
import time
from datetime import datetime


def generate_sensor_reading():

    # Normal sensor values
    temperature = 45.0
    humidity = 55.0
    vibration = 0.3
    battery = 85.0

    # Simulate an abnormal reading
    temperature = 85.0
    vibration = 0.95

    if temperature > 80:
        status = "HIGH_TEMPERATURE"
    elif vibration > 0.9:
        status = "HIGH_VIBRATION"
    else:
        status = "NORMAL"

    reading = {
        "source": "IOT_SENSOR",
        "timestamp": datetime.now().isoformat(),
        "temperature": temperature,
        "humidity": humidity,
        "vibration": vibration,
        "battery": battery,
        "status": status
    }

    print()
    print("================================")
    print(" ARTIFICIAL IOT SENSOR")
    print("================================")

    print()
    print("Sensor Reading")
    print("--------------------------------")
    print("Timestamp   :", reading["timestamp"])
    print("Temperature :", reading["temperature"], "°C")
    print("Humidity    :", reading["humidity"], "%")
    print("Vibration   :", reading["vibration"])
    print("Battery     :", reading["battery"], "%")
    print("Status      :", reading["status"])

    # Create failure file when anomaly occurs
    if status != "NORMAL":

        failure_data = {
            "source": "IOT_SENSOR",
            "failure_type": status,
            "timestamp": reading["timestamp"],
            "temperature": temperature,
            "humidity": humidity,
            "vibration": vibration,
            "battery": battery
        }

        with open("iot_failure.json", "w") as file:
            json.dump(failure_data, file, indent=4)

        print()
        print("⚠ SENSOR ANOMALY DETECTED")
        print("Failure Type :", status)

    return reading


if __name__ == "__main__":
    generate_sensor_reading()