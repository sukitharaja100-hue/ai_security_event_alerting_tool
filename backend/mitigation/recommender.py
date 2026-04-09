def recommend_action(risk):
    if risk > 80:
        return "Block IP and lock account"
    elif risk > 60:
        return "Force password reset"
    return "Monitor activity"
