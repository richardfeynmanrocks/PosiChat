from . import app
from flask import request
import time

@app.route('/message', methods=['POST'])
def on_message():
	try:
		post_data = request.form
		uname = post_data.get('username')
		content = post_data.get('content')
		sendtime = post_data.get('sendtime')
		recvtime = time.time()
		app.databases['messages'].add_entry((uname, content, sendtime, recvtime))
		return 200
	except:
		return 500

@app.route('/retrieve_message', methods=['POST'])
def retrieve_message():
	'''Send back the last 100 messages'''
	app.databases['messages'].get_last_n_entries(100)
