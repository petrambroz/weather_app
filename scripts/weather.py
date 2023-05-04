from datetime import datetime
from typing import Any


def convert_time(unix_timestamp: float) -> str:
    """converts unix timestamp to a readable format"""
    local_time = datetime.fromtimestamp(unix_timestamp)
    return local_time.strftime("%H:%M")


class Weather():
    """displays weather values for city. more to be added"""

    def process(self, response: dict[str, Any]) -> None:
        """
        extracts relevant data from servers response and saves them
        to a variable
        """
        self.city: str = response["name"]
        self.description: str = response["weather"][0]["description"]
        self.temp_min: int = round(response["main"]["temp_min"])
        self.temp_max: int = round(response["main"]["temp_max"])
        self.wind: int = round(response["wind"]["speed"])
        self.img_id: int = response["weather"][0]["icon"]
        self.img_url: str = ("https://openweathermap.org/img/wn/"
                             + str(self.img_id) + "@2x.png")
        self.sunrise: str = convert_time(response["sys"]["sunrise"])
        self.sunset: str = convert_time(response["sys"]["sunset"])
        return
