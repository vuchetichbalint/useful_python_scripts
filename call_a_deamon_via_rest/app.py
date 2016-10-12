#!flask/bin/python

"""
This REST API calling has been learnt here:
https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
import shlex, subprocess

import os

app = Flask(__name__)
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
	if username == 'miguel':
		return 'python'
	return None

@auth.error_handler
def unauthorized():
	return make_response(jsonify( { 'error': 'Unauthorized access' } ), 403)
	# return 403 instead of 401 to prevent browsers from displaying the default auth dialog
	
@app.errorhandler(400)
def not_found(error):
	return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify( { 'error': 'Not found' } ), 404)

@app.route('/perform', methods = ['GET'])
#@auth.login_required
def perform_action():
	print(os.getcwd())
	parameters = request.args.to_dict()
	try:
		action = parameters['action']
		
		if action in ['start', 'stop', 'restart']:
			command_line = 'python mydaemon.py ' + action
			args = shlex.split(command_line)
			p = subprocess.Popen(args)
		else:
			raise NameError('Wrong parameter!')
		
		return jsonify({'performing an action':action})
	
	except KeyError as e:
		return jsonify({'error':'missing parameter ' + str(e)})
	except Exception as e:
		return jsonify({'error': str(e)})

if __name__ == '__main__':
	app.run(debug=True)

