def predict_failure(sensor):

    print("\n====================================")
    print("        AI PREDICTION AGENT")
    print("====================================")

    if sensor is None:
        print("No sensor data available.")
        return None

    temperature = sensor["temperature"]
    humidity = sensor["humidity"]
    vibration = sensor["vibration"]
    voltage = sensor["voltage"]
    current = sensor["current"]

    risk_level = "LOW"
    failure_type = "NONE"

    # Check sensor conditions
    if temperature > 80:
        risk_level = "HIGH"
        failure_type = "HIGH_TEMPERATURE"

    elif vibration > 8:
        risk_level = "HIGH"
        failure_type = "HIGH_VIBRATION"

    elif voltage < 200 or voltage > 250:
        risk_level = "HIGH"
        failure_type = "VOLTAGE_ANOMALY"

    elif current > 15:
        risk_level = "HIGH"
        failure_type = "HIGH_CURRENT"

    elif humidity > 90:
        risk_level = "MEDIUM"
        failure_type = "HIGH_HUMIDITY"

    print(f"Risk Level  : {risk_level}")
    print(f"Failure Type: {failure_type}")

    return {
        "risk_level": risk_level,
        "failure_type": failure_type
    }


if __name__ == "__main__":
    print("Predict Agent ready.")
