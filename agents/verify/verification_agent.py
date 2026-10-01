from datetime import datetime


def verify_recovery(recovery_result):

    print("\n====================================")
    print("       VERIFICATION AGENT")
    print("====================================")

    if recovery_result is None:
        print("No recovery was performed.")
        return "NOT_REQUIRED"

    recovery_status = recovery_result.get("status")

    if recovery_status == "RECOVERY_COMPLETED":
        verification_status = "VERIFIED"

    else:
        verification_status = "VERIFICATION_FAILED"

    print(f"Recovery Status     : {recovery_status}")
    print(f"Verification Status : {verification_status}")
    print(f"Verification Time   : {datetime.now().isoformat()}")

    return verification_status


if __name__ == "__main__":
    print("Verification Agent ready.")
