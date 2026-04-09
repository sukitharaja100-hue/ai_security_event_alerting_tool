def check_anomaly(event):
    attempts = event["attempts"]
    if attempts > 10:
        return 0.9
    elif attempts > 5:
        return 0.6
    return 0.2
