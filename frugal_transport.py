import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash

DATABASE = '/tmp/frugal_transport.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default' 


app = Flask(__name__)

@app.route('/')
def home():
    return ('yo')

if __name__ == "__main__":
    app.run()
