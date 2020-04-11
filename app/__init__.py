from flask import Flask

app = Flask(__name__) #Declare before the next import statement to solve import errors.

from app_methods import *
from classes import Databases, Database

def db():
	'''Run to set up the databases'''
	app.databases = Databases()
	app.databases.add(Database("messages"))
	app.databases.add(Database("users"))

def run(*args, **kwargs):
	app.run(*args, **kwargs)
