#!/usr/bin/python3
"""data base storage"""
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
import os
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base

class DBStorage:
  """a class that represebts the database"""
  __engine = None
  __session = None
  
  def __init__(self):
    user = os.environ.get('HBNB_MYSQL_USER')
    pwd = os.environ.get('HBNB_MYSQL_PWD')
    host = os.environ.get('HBNB_MYSQL_HOST', 'localhost')
    db = os.environ.get('HBNB_MYSQL_DB')
    self.__engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@{host}/{db}',
                                       pool_pre_ping=True)
    if os.environ.get('HBNB_ENV') == 'test':
      Base.metadata.drop_all(self.__engine)
