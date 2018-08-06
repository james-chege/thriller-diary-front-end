"""
Code for rendering the views
"""
from functools import wraps
from flask import request, render_template

from app import app


@app.route('/')
def index():
    """
    Render the index page
    """
    return render_template("index.html")

@app.route('/signup')
def signup():
    """
    Render the signup page
    """
    return render_template("sign-up.html")

@app.route('/signin')
def signin():
    """
    Render the signin page
    """
    return render_template("sign-in.html")