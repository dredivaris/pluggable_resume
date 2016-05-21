

class APIException(Exception):
    pass


class InvalidDataException(APIException):
    pass


class NotFoundException(Exception):
    pass
