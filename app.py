# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/20
🚀 Welcome to the Awesome Python Script 🚀

User: mesabo
Email: mesabo18@gmail.com / messouaboya17@gmail.com
Github: https://github.com/mesabo
Univ: Hosei University
Dept: Science and Engineering
Lab: Prof YU Keping's Lab

"""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", content="Hello World!")


@app.route("/<usr>")
def user(usr):
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["login-email"]
        return redirect(url_for("home", usr=user))
    else:
        return render_template("login.html")


if __name__ == '__main__':
    app.run()
