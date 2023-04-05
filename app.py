from flask import Flask, render_template
import requests
from dotenv import load_dotenv
from os import getenv
load_dotenv()
app = Flask(__name__)


class Weather():
    city = "a"
    temp = 0


@app.route("/")
def index():
    city = "Praha"
    const_url = "https://api.openweathermap.org/data/2.5/weather?units=metric"
    response = requests.post(const_url+"&q="+city+"&appid="+getenv("API_KEY"))
    weather_data = response.json()
    weather = Weather()
    weather.city = city
    weather.temp = weather_data["main"]["temp"]
    return render_template('index.html', weather=weather)


if __name__ == "__main__":
    app.run(debug=True)
