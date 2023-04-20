#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.city import City
import models
from os import getenv
from sqlalchemy.orm import relationship

class State(BaseModel, Base):

    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="delete", backref="state")
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """ cities getter attribute """
            list_city = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    list_city.append(city)
            return list_city
