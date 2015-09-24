import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine



Base = declarative_base()

engine = create_engine('sqlite:///restaurantmenu.db')




class Restaurant(Base):
    # # Clear Table name to be given . __tablename__ is a special variable
    __tablename__ = 'restaurant'

    # Table structure to be created.#
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)



class MenuItem(Base):
    __tablename__ = 'menu_item'


    #Table structure to be created.
    name = Column(String(80), nullable= False)
    id = Column(Integer, primary_key=True )
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)


Base.metadata.create_all(engine)