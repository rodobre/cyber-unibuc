from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_uri = "sqlite:///database.sql?check_same_thread=False"
engine = create_engine(db_uri)

Base = declarative_base()
Session = sessionmaker(bind = engine)