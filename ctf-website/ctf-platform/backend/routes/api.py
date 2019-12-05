#!/usr/bin/python3
from flask import Blueprint, render_template, send_file, jsonify, request
api_blueprint = Blueprint('api', __name__)

from db import Session
from db.db import Challenge, User
from routes.auth import is_authenticated
from base64 import b64decode
from sqlalchemy import exists
from html import escape
import json
import hashlib

@api_blueprint.route('/api/leaderboard', methods=['GET'])
def leaderboard():
	s = Session()
	users = s.query(User).all()
	user_list = []

	for user in users:
		user_points = 0

		for chall in user.solves:
			user_points += int(chall.points)

		user_list += [{'name':user.name, 'points':int(user_points)}]

	return jsonify({'leaderboard':sorted(user_list, key = lambda i: i['points'], reverse=True)})

@api_blueprint.route('/api/challenges', methods=['GET'])
def challenges():
	is_auth = False
	authcookie = None
	if 'authcookie' in request.cookies:
		authcookie = json.loads(b64decode(request.cookies.get('authcookie')))
		if is_authenticated(authcookie):
			is_auth = True

	s = Session()
	challenges = s.query(Challenge).order_by(Challenge.points.desc()).all()

	u = None
	solves = None

	if is_auth:
		u = s.query(User).filter_by(name = authcookie['user']).first()
		solves = u.solves

	challenge_list = []

	for challenge in challenges:
		chall = {}
		chall['title'] = escape(challenge.name, quote=True)
		chall['points'] = escape(challenge.points, quote=True)
		chall['desc'] = escape(challenge.desc, quote=True)
		chall['url'] = escape(challenge.url, quote=True)
		chall['id'] = challenge.id

		if is_auth:
			if challenge in solves:
				chall['solved'] = 1
			else:
				chall['solved'] = 0
		else:
			chall['solved'] = 0

		challenge_list += [chall]

	challenges_json_list = {'challenges':challenge_list}
	return jsonify(challenges_json_list)

@api_blueprint.route('/api/submit_flag', methods=['POST'])
def submit():
	is_auth = False
	authcookie = None
	if 'authcookie' in request.cookies:
		authcookie = json.loads(b64decode(request.cookies.get('authcookie')))
		if is_authenticated(authcookie):
			is_auth = True

	if not is_auth:
		return 'Not logged in', 403

	parameters = request.json
	if not 'challenge' in parameters or not 'flag' in parameters:
		return 'Invalid request', 400

	challenge_id = parameters['challenge']
	input_flag = parameters['flag']

	s = Session()
	challenge = s.query(Challenge).filter_by(id = challenge_id).first()

	if not challenge.verify(input_flag):
		return 'Invalid flag', 401

	r = s.query(User).filter_by(name = authcookie['user']).first()

	if challenge not in r.solves:
		r.solves.append(challenge)
		s.commit()
	else:
		return 'Already solved', 302
	return 'OK', 200