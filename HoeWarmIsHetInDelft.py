import requests

from exceptions import raise_if_failure, BaseAppError
from parsing import extract_temperature

WEATHER_URL = "https://weerindelft.nl/WU/55ajax-dashboard-testpage.php"


def retrieve_weather():
    try:
        temperature = process_response(requests.get(WEATHER_URL))
        print(f'Temperature is {temperature}°C.')
    except BaseAppError as error:
        print(f'The following exception has occurred: {type(error).__name__}')


def process_response(response):
    raise_if_failure(response)
    return extract_temperature(response.text)


if __name__ == '__main__':
    retrieve_weather()
