import unittest

from exceptions import ParsingError
from parsing import extract_temperature


class TestParsing(unittest.TestCase):
    def test_returns_temperature(self):
        response = ' \
        <span class="ajax" id="ajaxthermometer"> \
        <img alt="Currently 2.4°C, Max: 3.1°C, Min: 2.0°C" height="170" \
        src="thermometer.php?t=2.4°C" \
        title="Currently 2.4°C, Max: 3.1°C, Min: 2.0°C" width="54"> </img></span> \
        '

        temp = extract_temperature(response)

        self.assertEqual(temp, 2)

    def test_raises_exception(self):
        response = ''

        with self.assertRaises(ParsingError) as error:
            temp = extract_temperature(response)
        self.assertIn('error while parsing the response', error.exception.description)
