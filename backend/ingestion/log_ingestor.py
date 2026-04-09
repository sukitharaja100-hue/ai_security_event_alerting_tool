import json
from database.db_connection import get_connection


FAILED_THRESHOLD = 3   # Brute-force threshold


def calculate_risk(status, failed_count):
    """
    Risk scoring logic:
    SUCCESS = low risk
    FAILED = medium risk
    Multiple FAILED = high risk
    """

    if status == "SUCCESS":
        return 10

    if status == "FAILED":
        if failed_count >= FAILED_THRESHOLD:
            return 90   # High risk (Brute force)
        return 50       # Medium risk

    return 0


def ingest_logs():
    conn = get_connection()
    cursor = conn.cursor()

    # Track failed attempts per IP
    failed_ip_counter = {}

    with open("backend/logs/incoming_logs.json", "r") as f:
        logs = json.load(f)

    for log in logs:
        username = log["username"]
        ip = log["ip"]
        status = log["status"]
        time = log["time"]

        # Count failed attempts per IP
        if status == "FAILED":
            failed_ip_counter[ip] = failed_ip_counter.get(ip, 0) + 1
        else:
            failed_ip_counter[ip] = 0

        risk_score = calculate_risk(status, failed_ip_counter[ip])

        cursor.execute(
            """
            INSERT INTO logs (username, ip, status, time, risk_score)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (username, ip, status, time, risk_score)
        )

    conn.commit()
    conn.close()

    print("Logs ingested successfully with risk scoring.")
