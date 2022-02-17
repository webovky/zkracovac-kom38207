from . import app
from .models import User
from flask import render_template, request, redirect, url_for, session
import functools
from pony.orm import db_session

# from werkzeug.security import check_password_hash

slova = ("Super", "Perfekt", "Úža", "Flask")


def prihlasit(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        if "user" in session:
            return function(*args, **kwargs)
        else:
            return redirect(url_for("login", url=request.path))

    return wrapper


@app.route("/", methods=["GET"])
@db_session
def index():
    shorcut = request.args.get('shorcut')
    if shorcut and Addresses.get(shorcut=shorcut):
        # shorcut je v DB
        pass
    else:
        shocut = None
    return render_template("base.html.j2", shorcut=shorcut)

@app.route("/", methods=["POST"])
@db_session
def index_post():
    url = request.form.get("url")
    if url:
        shorcut = "".join([random.choice(string.ascii_letters) for i in range(7)])
        address = Address.get(shortcut=shortcut)
        while address is not None:
            shorcut = "".join([random.choice(string.ascii_letters) for i in range(7)])
            address = Address.get(shortcut=shortcut)

        if 'nick' in session:
            address = Addresses(url=url, shorcut=shorcut, user=User.get(nick=session['nick']))
        else:
            address = Addresses(url=url, shorcut=shorcut)

@app.route("/info/")
def info():
    return render_template("info.html.j2")


@app.route("/abc/")
def abc():
    return render_template("abc.html.j2", slova=slova)


@app.route("/text/")
def text():
    return """

<h1>Text</h1>

<p>toto je text</p>

"""
