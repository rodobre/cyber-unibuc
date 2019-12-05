from db import Session
from db.db import Challenge, User
import hashlib

def add_challenge(name, points, desc, flag, url):
	hashed_flag = hashlib.sha512(flag.lower().encode('utf-8')).hexdigest()
	c = Challenge(name = name, points = points, desc = desc, flag = hashed_flag, url = url)
	s = Session()
	s.add(c)
	s.commit()

def remove_challenge(name):
	c = Challenge(name = name)
	s = Session()
	s.query(Challenge).filter_by(name = name).delete()
	s.commit()

def show_challenge(name):
	c = Challenge(name = name)
	s = Session()
	r = s.query(Challenge).filter_by(name = name).all()
	print(r)

import sys
if __name__ == '__main__':
	args = sys.argv
	print(args)
	option = int(args[1])

	if option == 0:
		name = args[2]
		points = int(args[3])
		desc = args[4]
		flag = args[5]
		url = args[6]
		add_challenge(name, points, desc, flag, url)
	elif option == 1:
		name = args[2]
		remove_challenge(name)
	elif option == 2:
		name = args[2]
		show_challenge(name)
