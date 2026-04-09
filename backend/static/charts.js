document.addEventListener("DOMContentLoaded", function () {

    const riskCounts = { Low: 0, Medium: 0, High: 0 };
    const ipMap = {};
    const timeMap = {};

    alertsData.forEach(alert => {

        // Risk calculation
        if (alert.risk >= 70) riskCounts.High++;
        else if (alert.risk >= 40) riskCounts.Medium++;
        else riskCounts.Low++;

        // IP count
        ipMap[alert.ip] = (ipMap[alert.ip] || 0) + 1;

        // Date-wise count
        const date = alert.time.split(" ")[0];
        timeMap[date] = (timeMap[date] || 0) + 1;
    });

    new Chart(document.getElementById("riskChart"), {
        type: "pie",
        data: {
            labels: ["Low", "Medium", "High"],
            datasets: [{ data: Object.values(riskCounts) }]
        }
    });

    new Chart(document.getElementById("ipChart"), {
        type: "bar",
        data: {
            labels: Object.keys(ipMap),
            datasets: [{ label: "Failed Attempts", data: Object.values(ipMap) }]
        }
    });

    new Chart(document.getElementById("timeChart"), {
        type: "line",
        data: {
            labels: Object.keys(timeMap),
            datasets: [{ label: "Alerts Over Time", data: Object.values(timeMap) }]
        }
    });
});
