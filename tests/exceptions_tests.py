import unittest
from unittest.mock import Mock

from exceptions import raise_if_failure, CommunicationError


class TestExceptions(unittest.TestCase):
    def test_raises_exception_when_error_status_code(self):
        response = Mock(status_code=404)

        with self.assertRaises(CommunicationError) as error:
            raise_if_failure(response)
        self.assertIn('404', error.exception.description)