from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#This is the engine
engine = create_engine('sqlite:///pulse.db',echo=True)
#The waiting room
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()