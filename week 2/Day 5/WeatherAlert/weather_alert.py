import requests
from config import API_KEY
from models import Weather, session

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        desc = data["weather"][0]["description"]
        return {"city": city, "temp": temp, "humidity": humidity, "desc": desc}
    else:
        print("Erreur:", data.get("message"))
        return None

def save_to_db(info):
    weather = Weather(city=info["city"], temperature=info["temp"],
                      humidity=info["humidity"], weather_desc=info["desc"])
    session.add(weather)
    session.commit()

def check_alert(info):
    if "rain" in info["desc"] or "storm" in info["desc"]:
        print(f"⚠️ Alerte météo à {info['city']}: {info['desc'].capitalize()}")
    else:
        print(f"✅ Météo normale à {info['city']}: {info['desc']}")

def run(city):
    info = get_weather(city)
    if info:
        save_to_db(info)
        check_alert(info)
        print(f"🌡️ {info['temp']}°C | 💧 {info['humidity']}%")

if __name__ == "__main__":
    ville = input("Entrez une ville : ")
    run(ville)
