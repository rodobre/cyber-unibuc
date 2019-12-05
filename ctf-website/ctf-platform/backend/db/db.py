from . import Base, engine, Session
from sqlalchemy import Column, Integer, String, ForeignKey, exists, Table
from sqlalchemy.orm import relationship
import json
import hashlib

solutions_table = Table('solutions', Base.metadata, Column('user_id', Integer, ForeignKey('user.id')),
								Column('challenge_id', Integer, ForeignKey('challenge.id')))

class Challenge(Base):
	__tablename__ = "challenge"

	id = Column(Integer, primary_key = True)
	name = Column(String)
	points = Column(String)
	desc = Column(String)
	flag = Column(String)
	url = Column(String)
	solvers = relationship('User', secondary=solutions_table, back_populates='solves')

	def __repr__(self):
		return json.dumps({'id': self.id, 'title':self.name, 'points':self.points, 'desc':self.desc, 'url':self.url, 'flag':self.flag})

	def verify(self, input_flag):
		hashed_flag = hashlib.sha512(input_flag.lower().encode('utf-8')).hexdigest()
		if hashed_flag == self.flag:
			return True
		return False

class User(Base):
	__tablename__ = "user"

	id = Column(Integer, primary_key = True)
	name = Column(String)
	password = Column(String)
	solves = relationship('Challenge', secondary=solutions_table, back_populates='solvers')

	def __repr__(self):
		return json.dumps({'id':self.id, 'name':self.name, 'password':self.password})

	def hash_password(input_password):
		hashed_password = hashlib.sha512(input_password.encode('utf-8')).hexdigest()
		return hashed_password

	def auth(self, input_password):
		if input_password == self.password:
			return True
		return False

	def auth_plain(self, input_password):
		hashed_password = hashlib.sha512(input_password.encode('utf-8')).hexdigest()
		if hashed_password == self.password:
			return True
		return False

	def does_exist(username):
		s = Session()
		return s.query(exists().where(User.name == username)).scalar()

Base.metadata.create_all(engine)