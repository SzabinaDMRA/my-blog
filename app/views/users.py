from flask import request, redirect, url_for, render_template, abort
from app.controllers import UserLogin, GetCurrentUsername, UserLogout


def Login():
    if request.method == "POST":
        if request.form:
            if "username" in request.form and "password" in request.form:
                username = request.form["username"]
                password = request.form["password"]
                if UserLogin(username, password):
                    return redirect(url_for("Index"))
                else:
                    return redirect(url_for("Login"))
        abort(400)
    username, loginAuth = GetCurrentUsername()
    return render_template("login.html", username=username, login_auth=loginAuth)


def Logout():
    if UserLogout():
        return redirect(url_for("Index"))
