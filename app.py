"""
Small lightweight app for displaying weather.

It provides functionality for a basic webapp displaying weather 
in a selected city. When no city is requested, it defaults to
Prague.
"""
from os import getenv
from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)


class Weather():
    """displayed weather values for city. more to be added"""
    def __init__(self) -> None:
        self.city = ""
        self.description = ""
        self.temp = 0
        self.wind = 0
        self.img_id = 0
        self.img_url = ""
        self.img_url_base = "https://openweathermap.org/img/wn/"
    def process(self, response):
        """
        extracts relevant data from servers response and saves them
        to a variable
        """
        self.city = response["name"]
        self.description = response["weather"][0]["description"]
        self.temp = response["main"]["temp"]
        self.wind = response["wind"]["speed"]
        self.img_id = response["weather"][0]["icon"]
        self.img_url = "https://openweathermap.org/img/wn/" + str(self.img_id) + "@2x.png"
        return self

@app.route("/", methods=['POST', 'GET'])
def index():
    """
    index page, is default set to display weather in Prague.
    if POST is used, it loads city name from the form and displays that instead.
    """
    const_url = "https://api.openweathermap.org/data/2.5/weather?"
    units = "units=metric"
    language = "&lang=cz"
    if request.method == 'GET':
        city = "Praha"
    else:
        city = request.form['city']
    if " " in city:
        city = city.replace(" ", "+")
    response = requests.post(const_url+units+language+"&q="
                             + city +"&appid="
                             + getenv("API_KEY"), timeout=10)
    if response.status_code != 200:
        return "Město nenalezeno."
    instance=Weather
    return render_template('index.html',
                           weather=instance.process(instance,response.json()))


if __name__ == "__main__":
    app.run(debug=True)
