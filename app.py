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
from scripts.weather import Weather
load_dotenv()
app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index() -> str:
    """
    index page, is default set to display weather in Prague.
    if POST is used, it loads city name from the form and displays that instead
    """
    units = "units=metric"
    language = "&lang=cz"
    city = get_city()
    response = get_data(units, language, city)
    if response.status_code != 200:
        return "Město nenalezeno."
    instance = Weather()
    instance.process(response.json())
    return render_template('index.html', weather=instance)


def get_data(units: str, language: str, city: str):
    """gets a response from the openweather api"""
    const_url = "https://api.openweathermap.org/data/2.5/weather?"
    response = requests.post(const_url+units+language+"&q="
                             + city + "&appid="
                             + str(getenv("API_KEY")), timeout=10)
    return response


def get_city() -> str:
    """
    if no city is entered (on first page load), Prague is
    selected, otherwise city name gets loaded from form

    in case of a multi-word city name, the spaces get
    replaced by '+' sign so the api can understand it
    """
    if request.method == 'GET':
        return "Praha"
    else:
        city = request.form['city']
    if " " in city:
        city = city.replace(" ", "+")
    return city


if __name__ == "__main__":
    app.run(debug=True)
