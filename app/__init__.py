from flask import Flask

def application():
    # Configure app
    app = Flask(__name__)

    # Import blueprints
    from app.routes.root import root
    from app.routes.uber import uber

    app.register_blueprint(root)
    app.register_blueprint(uber)

    return app
