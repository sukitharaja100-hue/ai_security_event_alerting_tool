def calculate_risk(event, anomaly_score):
    base_score = event["attempts"] * 10
    risk_score = base_score + int(anomaly_score * 30)
    return min(risk_score, 100)
