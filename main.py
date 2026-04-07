from flask import Flask, render_template, request

app = Flask(__name__)

sun_hours = {
    "NJ": 4.2, "NY": 4.0, "CA": 5.5, "TX": 5.0, "FL": 5.2,
    "PA": 4.0, "IL": 4.1, "AZ": 6.5, "NV": 6.0, "CO": 5.3
}

car_data = {
    "Tesla Model 3": {"battery": 57, "mpk": 4.0},
    "Tesla Model Y": {"battery": 75, "mpk": 3.5},
    "Chevy Bolt": {"battery": 66, "mpk": 3.7},
    "Hyundai Ioniq 5": {"battery": 77, "mpk": 3.8},
    "Ford Mach-E": {"battery": 88, "mpk": 3.0}
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        state = request.form["state"]
        car = request.form["car"]
        miles = float(request.form["miles"])

        sun = sun_hours[state]
        battery = car_data[car]["battery"]
        mpk = car_data[car]["mpk"]

        panel_kwh = 0.4 * sun
        daily_kwh = miles / mpk
        panels_daily = round(daily_kwh / panel_kwh)
        panels_full = round(battery / panel_kwh)

        panel_cost = 300
        install_cost = 200

        cost_daily = panels_daily * (panel_cost + install_cost)
        cost_full = panels_full * (panel_cost + install_cost)

        result = {
            "state": state,
            "car": car,
            "sun": sun,
            "battery": battery,
            "mpk": mpk,
            "panels_daily": panels_daily,
            "panels_full": panels_full,
            "cost_daily": cost_daily,
            "cost_full": cost_full
        }

    return render_template("index.html",
                           result=result,
                           states=sun_hours,
                           cars=car_data)

if __name__ == "__main__":
    app.run()
