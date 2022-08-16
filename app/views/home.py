from flask import render_template
from app.controllers import GetCurrentUsername


def Index():
    username, loginAuth = GetCurrentUsername()
    return render_template("index.html", username=username, login_auth=loginAuth)
