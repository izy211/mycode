#!/usr/bin/env python3
from flask import Flask, session, render_template, redirect, url_for, escape, request
app = Flask(__name__)

app.secret_key = "any random string"

@app.route("/")
def index():
    if "username" in session:
        username = session["username"]
        if 'visits' in session:
            session['visits'] = session.get('visits') + 1
        else:
            session['visits'] = 1
        visitno = f"Total visits: {session.get('visits')}"
        return f"Logged in as {username}, your lifetime visits are {visitno}<br><b><a href = '/logout'>Click here to log out</a></b>"
    return "You are not logged in!<br><a href = '/login'><b>Click here to log in</b></a>"

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form.get("username")
        return redirect(url_for("index"))
    return """
    <form action = "" method = "POST">
        <p><input type = text name = username></p>
        <p><input type = submit value = Login></p>
    </form>
    """

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))

@app.route("/delete-visits")
def delete_visits():
    if "username" in session:
        session.pop('visits', None)
        return f"Visits deleted, total hits counter reset!"
    return "You are not logged in!<br><a href = '/login'><b>Click here to log in</b></a>"

if __name__ == "__main__":
    app.run(port=5006)
