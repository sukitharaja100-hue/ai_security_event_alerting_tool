from database.db_connection import get_connection

def get_dashboard_data(query=None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True, buffered=True)

    # Total logs
    if query:
        cursor.execute("SELECT COUNT(*) as total FROM logs WHERE ip LIKE %s", (f"%{query}%",))
    else:
        cursor.execute("SELECT COUNT(*) as total FROM logs")
    total = cursor.fetchone()["total"]

    # Failed logins
    if query:
        cursor.execute("SELECT COUNT(*) as failed FROM logs WHERE status='FAILED' AND ip LIKE %s", (f"%{query}%",))
    else:
        cursor.execute("SELECT COUNT(*) as failed FROM logs WHERE status='FAILED'")
    failed = cursor.fetchone()["failed"]

    # High risk
    if query:
        cursor.execute("SELECT COUNT(*) as high_risk FROM logs WHERE risk_score >= 80 AND ip LIKE %s", (f"%{query}%",))
    else:
        cursor.execute("SELECT COUNT(*) as high_risk FROM logs WHERE risk_score >= 80")
    high_risk = cursor.fetchone()["high_risk"]

    # Unique IPs
    if query:
        cursor.execute("SELECT COUNT(DISTINCT ip) as unique_ips FROM logs WHERE ip LIKE %s", (f"%{query}%",))
    else:
        cursor.execute("SELECT COUNT(DISTINCT ip) as unique_ips FROM logs")
    unique_ips = cursor.fetchone()["unique_ips"]

    # Logs
    if query:
        cursor.execute("""SELECT * FROM logs WHERE username LIKE %s OR ip LIKE %s OR status LIKE %sORDER BY time DESC LIMIT 20""", (f"{query}%", f"%{query}%", f"%{query}%"))
    else:
        cursor.execute("SELECT * FROM logs ORDER BY time DESC LIMIT 20")
    logs = cursor.fetchall()

    # Failed vs Success count
    cursor.execute("""SELECT status, COUNT(*) as count FROM logs GROUP BY status""")
    status_data = cursor.fetchall()

    # Timeline data (last 10 timestamps)
    if query:
        cursor.execute("""SELECT DATE_FORMAT(time, '%H:%i') as t, COUNT(*) as count FROM logs WHERE ip LIKE %s GROUP BY t ORDER BY t DESC LIMIT 10""", (f"%{query}%",))
    else:
        cursor.execute("""SELECT DATE_FORMAT(time, '%H:%i') as t, COUNT(*) as count FROM logs GROUP BY t ORDER BY t DESC LIMIT 10""")
    timeline = cursor.fetchall()

    # Top attacker IPs
    if query:
        cursor.execute("""SELECT ip, COUNT(*) as count FROM logs WHERE ip LIKE %s GROUP BY ip ORDER BY count DESC LIMIT 5""", (f"%{query}%",))
    else:
        cursor.execute("""SELECT ip, COUNT(*) as count FROM logs GROUP BY ip ORDER BY count DESC LIMIT 5""")
    top_ips = cursor.fetchall()

    conn.close()

    return {
    "total": total or 0,
    "failed": failed or 0,
    "high_risk": high_risk or 0,
    "unique_ips": unique_ips or 0,
    "logs": logs or [],
    "status_data": status_data or [],
    "timeline": timeline or [],
    "top_ips": top_ips or []
}