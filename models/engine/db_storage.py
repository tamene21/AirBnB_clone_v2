#!/usr/bin/python3
"""
Contains the DBStorage class
"""

import models
from models.amenity import Amenity
from models.base_model import Basemode, Base
from model.city import City
from model.place import Place
from model.review import Review
from model.state import State
from model.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
froom sqlalchemy.orm import scoped_session, sessionmaker


classes = {"Amentity": Amenity, "city": City, "place": Place,
            "Review":Review, "State": State, "User": User}

class DBStorage:
    """Interacts with MySQL DB"""
    def __init__(self):
        """Instantiate a DBStorage object"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)




    def close(self):
        """Call a private remove() session attribute""" 
        self.__session.remove()
