from database.db_connection import get_connection
from config import FAILED_LOGIN_THRESHOLD

def detect_attacks():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT username, ip, COUNT(*) as attempts
        FROM logs
        WHERE status='FAIL'
        GROUP BY username, ip
        HAVING attempts >= %s
    """, (FAILED_LOGIN_THRESHOLD,))

    results = cursor.fetchall()
    conn.close()
    return results
