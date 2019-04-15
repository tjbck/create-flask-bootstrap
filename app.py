from flask import Flask, request, render_template
app = Flask(__name__)
app.secret_key = 'Your_New_App!'
app.debug = True

import time
import json
import datetime as dt

@app.route('/')
def index():
    return "DASOMI"
