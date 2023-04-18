#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os

# check if HBNB_TYPE_STORAGE environment variable is set to "db"
if os.getenv('HBNB_TYPE_STORAGE') == "db":
  storage = DBStorage()
else:
  storage = FileStorage()
  
# load stored data (if any)
storage.reload()
