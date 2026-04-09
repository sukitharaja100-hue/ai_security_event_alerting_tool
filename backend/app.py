from flask import Flask, render_template
from flask import Flask, render_template, request
from dashboard.dashboard_queries import get_dashboard_data

app = Flask(__name__, template_folder="templates")


@app.route("/", methods=["GET"])
def dashboard():
    query = request.args.get("q")

    data = get_dashboard_data(query)

    if not data:
        data = {
            "total": 0,
            "failed": 0,
            "high_risk": 0,
            "unique_ips": 0,
            "logs": [],
            "status_data": [],
            "timeline": [],
            "top_ips": []
        }

    return render_template("dashboard.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)