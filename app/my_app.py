from flask import Flask
from .controllers import MySessionInterface
from .views import Index as _Index, Login as _Login, Logout as _Logout
from .views import Contact as _Contact, ContactList as _ContactList


def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.secret_key = b"?8jyhf73hf"
    app.config.from_pyfile("config.py")
    app.session_interface = MySessionInterface()

    if app.config["VERSION"] == "1.0.1":
        pass
    elif app.config["VERSION"] == "1.0.2":
        pass

    @app.route("/")
    def Index():
        return _Index()

    @app.route("/login", methods=["GET", "POST"])
    def Login():
        return _Login()

    @app.route("/logout")
    def Logout():
        return _Logout()

    @app.route("/contact", methods=["GET", "POST"])
    def Contact():
        return _Contact()

    @app.route("/list")
    def ContactList():
        return _ContactList()

    return app
