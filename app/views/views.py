from flask import Flask, render_template, redirect, url_for, request, abort
from app.controllers import MySessionInterface
from app.controllers import UserLogin, UserLogout, GetCurrentUsername
from app.controllers import GetContactList, SaveContactRequest

app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.secret_key = b"?8jyhf73hf"
app.session_interface = MySessionInterface()


@app.route("/")
def Index():
    username, loginAuth = GetCurrentUsername()
    return render_template("index.html", username=username, login_auth=loginAuth)


@app.route("/contact", methods=["GET", "POST"])
def Contact():
    if request.method == "POST":
        if request.form:
            name = request.form.get("name")
            email = request.form.get("email")
            category = request.form.get("category")
            priority = request.form.get("priority")
            message = request.form.get("message")

            SaveContactRequest(name, email, category, priority, message)

            return redirect(url_for("Contact"))

    username, loginAuth = GetCurrentUsername()

    return render_template("contact.html", username=username, login_auth=loginAuth)


@app.route("/contactlist")
def ContactList():
    username, loginAuth = GetCurrentUsername()
    contactList = GetContactList()
    return render_template("contact_list.html", username=username, login_auth=loginAuth, contactList=contactList)


@app.route("/login", methods=["GET", "POST"])
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


@app.route("/logout")
def Logout():
    if UserLogout():
        return redirect(url_for("Index"))
