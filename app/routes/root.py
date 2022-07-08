from flask import Blueprint

root = Blueprint('api', __name__, url_prefix="/")


@root.route("/")
def index():
    return "Hello Palenca!"
