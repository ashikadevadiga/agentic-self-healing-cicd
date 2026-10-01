import json

SENSOR_FILE = "iot/sensor_data.json"

def monitor_sensor():
    print("====================================")
    print("        IOT SENSOR MONITOR")
    print("====================================")

    try:
        with open(SENSOR_FILE, "r") as file:
            data = json.load(file)

        # Handle sensor data stored as a list
        if isinstance(data, list):
            if not data:
                print("ERROR: sensor_data.json is empty.")
                return None

            # Use the latest sensor reading
            sensor = data[-1]
        else:
            sensor = data

        print(f"Timestamp   : {sensor['timestamp']}")
        print(f"Temperature : {sensor['temperature']}")
        print(f"Humidity    : {sensor['humidity']}")
        print(f"Vibration   : {sensor['vibration']}")
        print(f"Voltage     : {sensor['voltage']}")
        print(f"Current     : {sensor['current']}")
        print(f"Status      : {sensor['status']}")

        return sensor

    except FileNotFoundError:
        print("ERROR: sensor_data.json not found.")
        return None

    except KeyError as e:
        print(f"ERROR: Missing sensor field: {e}")
        return None

if __name__ == "__main__":
    monitor_sensor()
