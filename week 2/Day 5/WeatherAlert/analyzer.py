from models import Weather, session
import matplotlib.pyplot as plt
from io import BytesIO

def generate_chart(city):
    records = session.query(Weather).filter_by(city=city).order_by(Weather.timestamp).all()
    if not records:
        return None

    timestamps = [r.timestamp for r in records]
    temps = [r.temperature for r in records]

    fig, ax = plt.subplots()
    ax.plot(timestamps, temps, marker='o', linestyle='-', color='blue')
    ax.set_title(f"Tendance Température - {city}")
    ax.set_xlabel("Temps")
    ax.set_ylabel("Température (°C)")
    fig.autofmt_xdate()

    img = BytesIO()
    fig.savefig(img, format='png')
    plt.close(fig)
    img.seek(0)
    return img
