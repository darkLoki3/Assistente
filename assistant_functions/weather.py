from lib2to3.pgen2 import token
import pyowm

token = ""

own = pyowm.OWM(token).weather_manager()


def get_weather():
    zip_code = "91900790"
    weather = own.weather_at_zip_code(zip_code, 'BR').weather
    temperature = int(round(weather.temperature(unit='celsius')['temp'], 0))
    return f"Atualmente, a temperatura é {temperature} degrees"
