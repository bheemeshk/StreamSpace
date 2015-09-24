__author__ = 'bheem'


import sqlite3

db_conn = sqlite3.connect('test.db')

cur = db_conn.cursor()

cur.execute(
    '''DROP TABLE person
    ''')

cur.execute(
    '''DROP TABLE address
    ''')


cur.execute(
    '''CREATE TABLE person
        (id INTEGER PRIMARY KEY ASC, name VARCHAR(250) NOT NULL)
    ''')

cur.execute(
    '''CREATE TABLE address
        (id INTEGER PRIMARY KEY ASC, street_name varchar(250), street_number varchar(250),
        post_code varchar(5) NOT NULL, person_id INTEGER NOT NULL, FOREIGN KEY(person_id) REFERENCES person(id))
    ''')

cur.execute(
    ''' INSERT INTO person VALUES(1, 'Bheemesh')
    ''')

cur.execute(
    '''INSERT INTO address VALUES(1, 'Journal Sq, Ave', '623 Summit Ave', '08080', 1)
    ''')

db_conn.commit()




cur.execute('select * from person')
print(cur.fetchall())

cur.execute('select * from address')
print(cur.fetchall())





# SQL ALCHEMY STARTS HERE

from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker



Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Address(Base):
    __tablename__ = 'address'

    id=Column(Integer,primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(5))
    person_id = Column(Integer, ForeignKey(Person.id))
    person = relationship(Person)


engine = create_engine('sqlite:///test.db')

Base.metadata.create_all(engine)


Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


new_person = Person(name='Srilakshmi')
session.add(new_person)
session.commit()

new_address = Address(post_code='00000', person=new_person)
session.add(new_address)
session.commit()


printPerson = session.query(Person).first()

print(printPerson.name)