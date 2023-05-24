#!/usr/bin/python3
"""data base storage"""
from models.base_model import BaseModel, Base
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

classes = {
    'BaseModel': BaseModel, 'User': User, 'Place': Place,
    'State': State, 'City': City, 'Amenity': Amenity,
    'Review': Review
}
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
  def all(self, cls=None):
        """ all method """
        if not cls:
            objs = self.__session.query(State, City,
                                        Place, User, Amenity, Review).all()
        else:
            objs = self.__session.query(cls)
        final_dict = {}
        [final_dict.update({
            f"{type(item).__name__}.{item.id}": item
            }) for item in objs]
        return final_dict

  def new(self, obj):
      """ new method creates new object """
      self.__session.add(obj)

  def save(self):
      """ save method saves the object """
      self.__session.commit()

  def delete(self, obj=None):
      """ delete method deletes the object """
      if obj:
          self.__session.delete(obj)
          self.save()

  def reload(self):
      """ reload method creates a session """
      Base.metadata.create_all(self.__engine)
      session_factory = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
      Session = scoped_session(session_factory)
      self.__session = Session()

  def close(self):
      """ close method close the session """
      if self.__session:
          self.__session.close()
