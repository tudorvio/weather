import re

from bs4 import BeautifulSoup

from exceptions import ParsingError

CURRENT_TEMPERATURE_REGEX = r'Currently -?\d*\.?\d*'


def extract_temperature(response_body):
    soup = BeautifulSoup(response_body, "html.parser")
    thermometer_div = soup.find("span", {"id": "ajaxthermometer"})
    try:
        temps = re.findall(CURRENT_TEMPERATURE_REGEX, str(thermometer_div))
        return round(float(temps[0].split(' ')[1]))
    except IndexError:
        error_msg = 'Encountered an error while parsing the response.'
        print(error_msg)
        raise ParsingError(error_msg)
