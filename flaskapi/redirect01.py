#!/usr/bin/env python3
from flask import Flask, session, render_template, redirect, url_for, escape, request, abort
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('log_in.html')

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form['username'] == 'admin':
            return redirect(url_for('success'))
        else:
            abort(403, "Verboten!")
    else:
        return redirect(url_for('index'))

@app.route("/success")
def success():
    return "Logged in successfully!"

if __name__ == "__main__":
    app.run(port=5006)
