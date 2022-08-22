from flask import render_template, Blueprint
from app.controllers import GetCurrentUsername

bp = Blueprint("home", __name__, template_folder="../templates")


@bp.route("/")
def Index():
    username, loginAuth = GetCurrentUsername()
    return render_template("index.html", username=username, login_auth=loginAuth)
