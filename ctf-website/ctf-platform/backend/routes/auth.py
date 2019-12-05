#!/usr/bin/python3
from flask import Blueprint, render_template, send_file, jsonify, request, make_response
auth_blueprint = Blueprint('auth', __name__)

from secrets import token_bytes
from base64 import b64encode, b64decode
from db import Session
from db.db import Challenge, User
from html import escape
import hashlib
import json

from hmac_key import session_key

@auth_blueprint.route('/api/login', methods=['POST'])
def login():
	credentials = request.json
	print(credentials)

	if 'name' not in credentials and 'password' not in credentials:
		return 'Invalid register parameters', 400

	username = escape(credentials['name'], quote=True)
	password = credentials['password']

	r = User.does_exist(username)

	if not r:
		return 'Username or password incorrect', 401

	hashed_password = User.hash_password(password)
	u = User(name = username, password = hashed_password)
	s = Session()
	r = s.query(User).filter_by(name = username, password = hashed_password).first()


	if not r:
		return 'Username or password incorrect', 401

	if not u.auth(r.password):
		return 'Username or password incorrect', 401

	session_cookie = hashlib.sha512(session_key + hashlib.sha512(username.encode('utf-8')).digest()).digest()
	cookie_json = json.dumps({'user':username, 'session':b64encode(session_cookie).decode('utf-8')})
	cookie = b64encode(cookie_json.encode('utf-8')).decode('utf-8')
	resp = make_response('OK', 200)
	resp.set_cookie('authcookie', cookie)
	return resp

@auth_blueprint.route('/api/register', methods=['POST'])
def register():
	credentials = request.json
	print(credentials)

	if 'name' not in credentials and 'password' not in credentials:
		return 'Invalid register parameters', 400

	username = escape(credentials['name'], quote=True)
	password = credentials['password']

	r = User.does_exist(username)

	if r:
		return 'User already exists', 401

	u = User(name = username, password = User.hash_password(password))
	s = Session()
	s.add(u)
	s.commit()
	return 'OK', 200

def is_authenticated(session_json):
	username = session_json['user']
	session = session_json['session']

	hmac_user = hashlib.sha512(session_key + hashlib.sha512(username.encode('utf-8')).digest()).digest()
	hmac_encoded = b64encode(hmac_user).decode('utf-8')

	if hmac_encoded == session:
		return True
	return False

@auth_blueprint.route('/api/session_check', methods=['POST'])
def session_check():
	if 'authcookie' not in request.cookies:
		return 'Not logged in', 403

	try:
		user_cookie = request.cookies.get('authcookie')
		user_cookie = json.loads(b64decode(user_cookie))
	except:
		return 'Invalid session', 401

	auth_result = is_authenticated(user_cookie)

	if auth_result == True:
		return 'OK', 200
	return 'Invalid session', 401

@auth_blueprint.route('/logout', methods=['GET'])
def logout():
	resp = make_response('<script>window.location = "/home";</script>', 200)
	resp.set_cookie('authcookie', expires=0)
	return resp
