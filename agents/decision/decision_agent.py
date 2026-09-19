def make_decision(prediction_data):

    print()
    print("===== DECISION AGENT =====")

    risk_level = prediction_data.get("risk_level", "UNKNOWN")
    failure_type = prediction_data.get("failure_type", "UNKNOWN")

    print("Risk Level    :", risk_level)
    print("Failure Type  :", failure_type)

    if risk_level == "HIGH":
        decision = "FIX_AND_RETEST"

    elif risk_level == "MEDIUM":
        decision = "FIX_AND_RETEST"

    else:
        decision = "MONITOR"

    print("Decision      :", decision)

    return {
        "risk_level": risk_level,
        "failure_type": failure_type,
        "decision": decision
    }


if __name__ == "__main__":

    import json
    import os

    failure_file = "iot_failure.json"

    if os.path.exists(failure_file):

        with open(failure_file, "r") as file:
            prediction_data = json.load(file)

        # Add prediction-agent information
        prediction_data["risk_level"] = "HIGH"

        result = make_decision(prediction_data)

        print()
        print("===== DECISION RESULT =====")
        print(result)

    else:

        print("No IoT failure file found.")