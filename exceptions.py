HTTP_ERROR_STARTING_RANGE = 400


class BaseAppError(Exception):
    def __init__(self, desc=''):
        self.description = desc


class CommunicationError(BaseAppError):
    pass


class ParsingError(BaseAppError):
    pass


def raise_if_failure(response):
    if response.status_code > HTTP_ERROR_STARTING_RANGE:
        error_msg = f'Request failed with status code: {response.status_code}'
        print(error_msg)
        raise CommunicationError(error_msg)
