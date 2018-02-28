from flask import Flask, render_template
from application import app
from application import model
import sqlite3

booklist = model.booklist

@app.route('/')
@app.route('/index')
def index():
    return "Hello, world!"