from flask import Flask, render_template
from dashboard.dashboard_queries import get_dashboard_data

app = Flask(__name__, template_folder="../templates")

@app.route("/")
def home():
    return dashboard()

@app.route("/dashboard")
def dashboard():
    data = get_dashboard_data()
    
    # SAFETY FIX (important)
    if not data:
        data = {
            "total": 0,
            "failed": 0,
            "high_risk": 0,
            "unique_ips": 0,
            "logs": []
        }

    return render_template("dashboard.html", data=data)