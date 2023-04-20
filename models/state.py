#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.city import City
from models import storage
from os import getenv
from sqlalchemy.orm import relationship

class State(BaseModel, Base):

    """ State class """

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __table_name__= 'states'
        name = Column(String(128), nullabe=False)
        cities = relationship("City", cascade="delete", backref="state")
    else:
        @property
        def cities(self):
            """ cities getter attribute """
            list_city = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    list_city.append(city)
            return list_city
