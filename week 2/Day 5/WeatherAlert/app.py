from flask import Flask, render_template, request, jsonify
from weather_alert import get_weather, save_to_db, check_alert
from models import Weather, session
from analyzer import generate_chart
from flask import send_file

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form["city"]
        info = get_weather(city)
        if info:
            save_to_db(info)
            alert = "Oui" if "rain" in info["desc"] or "storm" in info["desc"] else "Non"
            return render_template("result.html", info=info, alert=alert)
        return render_template("index.html", error="Ville invalide")
    return render_template("index.html")

@app.route('/api/weather/<city>', methods=["GET"])
def get_city_weather(city):
    data = session.query(Weather).filter_by(city=city).all()
    if not data:
        return jsonify({"message": "Aucune donnée trouvée"}), 404
    return jsonify([
        {
            "city": d.city,
            "temp": d.temperature,
            "humidity": d.humidity,
            "description": d.weather_desc,
            "timestamp": d.timestamp
        } for d in data
    ])

@app.route('/api/weather', methods=["POST"])
def add_weather():
    city = request.json.get("city")
    if not city:
        return jsonify({"error": "Ville manquante"}), 400
    info = get_weather(city)
    if info:
        save_to_db(info)
        return jsonify({"message": "Météo ajoutée", "data": info}), 201
    return jsonify({"error": "Erreur de récupération"}), 500

@app.route('/api/weather/<city>/chart', methods=["GET"])
def city_weather_chart(city):
    chart = generate_chart(city)
    if not chart:
        return jsonify({"error": "Aucune donnée pour cette ville"}), 404
    return send_file(chart, mimetype='image/png')
 
if __name__ == "__main__":
    app.run(debug=True)
