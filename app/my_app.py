from flask import Flask
from .controllers import MySessionInterface
from .views import home, users, contacts


def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.secret_key = b"?8jyhf73hf"
    app.config.from_pyfile("config.py")
    app.session_interface = MySessionInterface()

    if app.config["VERSION"] == "1.0.1":
        pass
    elif app.config["VERSION"] == "1.0.2":
        pass

    app.register_blueprint(home.bp)
    app.register_blueprint(users.bp)
    app.register_blueprint(contacts.bp)
    return app
