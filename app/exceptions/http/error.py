from http import HTTPStatus
from flask import jsonify


class ErrorResponse:
    def __init__(self, http_status=HTTPStatus.INTERNAL_SERVER_ERROR, **data):
        self.data = data
        self.http_status = http_status

    def jsonify(self):
        return jsonify({"error": self.http_status.phrase, **self.data}), self.http_status.value
