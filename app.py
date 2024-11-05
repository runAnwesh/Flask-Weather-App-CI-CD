import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Free Weather App!"

@app.route("/weather")
def get_weather():
    city = request.args.get("city", "New Delhi")
    url = f"https://api.open-meteo.com/v1/forecast?latitude=28.6139&longitude=77.2088&current_weather=true"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            "temperature": data["current_weather"]["temperature"],
            "windspeed": data["current_weather"]["windspeed"],
        }
        return jsonify(weather)
    else:
        return jsonify({"error": "Unable to fetch weather data"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
