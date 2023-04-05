from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
from os import getenv
load_dotenv()
app = Flask(__name__)


class Weather():
    city = "a"
    temp = 0
    description = ""
    wind = 0


@app.route("/", methods=['POST', 'GET'])
def index():
    const_url = "https://api.openweathermap.org/data/2.5/weather?"
    url_args = "units=metric&lang=cz"
    if request.method == 'GET':
        city = "Praha"
    else:

        city = request.form['city']
    response = requests.post(const_url+url_args+"&q="
                             + city+"&appid="
                             + getenv("API_KEY"))
    print(response)
    if response.status_code != 200:
        return "Město nenalezeno."
    weather_data = response.json()
    weather = Weather()
    weather.city = weather_data["name"]
    weather.description = weather_data["weather"][0]["description"]
    weather.temp = weather_data["main"]["temp"]
    weather.wind = weather_data["wind"]["speed"]
    return render_template('index.html', weather=weather)


if __name__ == "__main__":
    app.run(debug=True)
