from flask import Blueprint, jsonify, request
from app.exceptions.http.unprocesable_entity import UnprocessableEntityResponse
from app.forms.login import LoginForm
from app.services.AuthService import AuthService

uber = Blueprint('uber', __name__, url_prefix="/uber")


@uber.route("/login", methods=["POST"])
def login():
    form = LoginForm()
    if not form.validate():
        return UnprocessableEntityResponse(fields=dict(form.errors.items())).jsonify()

    username = request.json.get("email")
    password = request.json.get("password")

    auth_service = AuthService(username, password)

    if not auth_service.authenticate():
        message = 'CREDENTIALS_INVALID'
        details = 'Incorrect username or password'
        return {"message": message, "details": details}

    message = "SUCCESS"
    access_token = auth_service.get_token()

    return {"message": message, "access_token": access_token}


@uber.route("/profile/<string:token>")
def profile(token):
    auth_service = AuthService()

    if not auth_service.check_token(token):
        message = 'CREDENTIALS_INVALID'
        details = 'Incorrect token'
        return {"message": message, "details": details}

    message = "SUCCESS"
    profile = auth_service.get_profile()
    return {"message": message, "profile": profile}
