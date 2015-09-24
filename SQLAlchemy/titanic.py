from sqlalchemy import Column, Integer, String, REAL
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///titanic.db')

class titanic(Base):
    __tablename__ = 'titanic'

    pclass = Column(String)
    survived = Column(String)
    name = Column(String, primary_key=True)
    sex = Column(String)
    age = Column(Integer)
    sibsp = Column(String)
    parch = Column(String)
    ticket = Column(String)
    fare = Column(REAL)
    cabin = Column(String)
    embarked = Column(String)
    boat = Column(String)
    body = Column(String)
    home_dest = Column(String)

Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


Data =  [rec.__dict__ for rec in session.query(titanic).all()]

print Data{'fare'}