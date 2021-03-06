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

@app.route('/dashboard')
def dashboard():
    """
    Render the dashboard page
    """
    return render_template("dashboard.html")

@app.route('/add')
def add():
    """
    Add new entry page rendering
    """
    return render_template("add.html")

@app.route('/entries')
def entries():
    """
    view all entries
    """
    return render_template("entries.html")

@app.route('/modify/<int:entryId>')
def modify(entryId):
    """
    Edit entry
    """
    return render_template("modify.html")

@app.route('/view/<int:entryId>')
def view(entryId):
    """
    Preview entry
    """
    return render_template("content.html")

@app.route('/profile')
def profile():
    """
    Preview profile
    """
    return render_template("profile.html")