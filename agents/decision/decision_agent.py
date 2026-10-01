def make_decision(risk_level, failure_type):

    print("\n====================================")
    print("        DECISION AGENT")
    print("====================================")

    if risk_level == "HIGH":
        action = "INITIATE_RECOVERY"

    elif risk_level == "MEDIUM":
        action = "MONITOR_CLOSELY"

    else:
        action = "NO_ACTION"

    print(f"Risk Level   : {risk_level}")
    print(f"Failure Type : {failure_type}")
    print(f"Action       : {action}")

    return action


if __name__ == "__main__":
    print("Decision Agent ready.")
