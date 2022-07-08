from http import HTTPStatus
from app.exceptions.http.error import ErrorResponse


class UnprocessableEntityResponse(ErrorResponse):
    def __init__(self, http_status=HTTPStatus.UNPROCESSABLE_ENTITY, **data):
        ErrorResponse.__init__(self, http_status=http_status, **data)
