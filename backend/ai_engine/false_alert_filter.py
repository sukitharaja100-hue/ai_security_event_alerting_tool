def is_false_alert(event):
    return event["attempts"] < 6
