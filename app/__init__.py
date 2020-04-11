from flask import Flask
from app_methods import *

app = Flask(__name__)

def run(*args, **kwargs):
	app.run(*args, **kwargs)
