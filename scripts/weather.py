from datetime import datetime, timedelta


class Weather():
    """displays weather values for city. more to be added"""
    def __init__(self) -> None:
        self.city = None
        self.description = None
        self.temp = None
        self.wind = None
        self.img_id = None
        self.img_url = None
        self.unix_sunrise = None
        self.sunrise = None
        self.sunset = None

    def convert_time(self, unix_timestamp) -> str:
        """converts unix timestamp to a readable format"""
        utc_time = datetime.utcfromtimestamp(unix_timestamp)
        return (utc_time + timedelta(hours=2)).strftime("%H:%M")

    def process(self, response) -> object:
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
        self.sunrise = self.convert_time(self, response["sys"]["sunrise"])
        self.sunset = self.convert_time(self, response["sys"]["sunset"])
        return self
