#from cProfile import run
from cProfile import run
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World'
app.run()

#export FLASK_APP=app.py
#set FLASK_APP=app.py
#flask run

#import datetime as dt
#import numpy as np
#import pandas as pd
