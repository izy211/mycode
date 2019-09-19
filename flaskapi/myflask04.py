#!/usr/bin/env python3
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route("/success/<name>")
def success(name):
    return f"Welcome, {name}!"

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("success", name = user))
    else:
        user = request.args.get("nm")
        return redirect(url_for("success", name = user))

@app.route("/start")
def start():
    return render_template("postmaker.html")

if __name__ == "__main__":
    app.run(port=5006, debug = True)
