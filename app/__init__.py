from flask import Flask

def application():
    # Configure app
    app = Flask(__name__)

    # Import blueprints
    from app.routes.root import root
    app.register_blueprint(root)

    return app
