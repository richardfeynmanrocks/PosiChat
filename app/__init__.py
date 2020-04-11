from flask import Flask

app = Flask(__name__) #Declare before the next import statement to solve import errors.

from app_methods import *

def run(*args, **kwargs):
	app.run(*args, **kwargs)
