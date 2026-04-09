from config import HIGH_RISK_SCORE

def should_send_alert(risk_score, false_alert):
    if false_alert:
        return False
    return risk_score >= HIGH_RISK_SCORE
