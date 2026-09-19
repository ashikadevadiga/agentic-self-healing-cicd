import json
import os


FAILURE_FILE = "iot_failure.json"


def predict_failure(monitor_data):

    print()
    print("===== PREDICT AGENT =====")

    failure_type = monitor_data.get("failure_type", "UNKNOWN")

    if failure_type == "HIGH_TEMPERATURE":

        prediction = "IoT temperature threshold exceeded"
        risk_level = "HIGH"
        confidence = 95

    elif failure_type == "HIGH_VIBRATION":

        prediction = "Abnormal vibration detected"
        risk_level = "HIGH"
        confidence = 93

    elif failure_type == "LOW_BATTERY":

        prediction = "IoT sensor battery level is critically low"
        risk_level = "MEDIUM"
        confidence = 90

    else:

        prediction = "Unknown IoT failure detected"
        risk_level = "MEDIUM"
        confidence = 70

    print("Prediction    :", prediction)
    print("Risk Level    :", risk_level)
    print("Confidence    :", str(confidence) + "%")
    print("Failure Type  :", failure_type)

    return {
        "prediction": prediction,
        "risk_level": risk_level,
        "confidence": confidence,
        "failure_type": failure_type
    }


if __name__ == "__main__":

    if os.path.exists(FAILURE_FILE):

        with open(FAILURE_FILE, "r") as file:
            monitor_data = json.load(file)

        result = predict_failure(monitor_data)

        print()
        print("===== PREDICTION RESULT =====")
        print(result)

    else:

        print("No IoT failure file found.")