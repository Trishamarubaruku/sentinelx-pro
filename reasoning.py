def reason(anomaly, data):
    cpu = data["cpu"]
    memory = data["memory"]

    explanation = ""

    if anomaly == "CRITICAL_ANOMALY":
        explanation = f"CPU is critically high at {cpu}%, system overload likely."
        decision = "RESTART_SERVICE"

    elif anomaly == "ANOMALY_DETECTED":
        explanation = f"Unusual pattern detected: CPU={cpu}, Memory={memory}"
        decision = "INVESTIGATE"

    else:
        explanation = "System operating normally."
        decision = "NO_ACTION"

    return decision, explanation