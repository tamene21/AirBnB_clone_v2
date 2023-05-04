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
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        HBNB_MYSQL_USER = getenv('hbnb_dev')
        HBNB_MYSQL_PWD = getenv('hbnb_dev_pwd')
        HBNB_MYSQL_HOST = getenv('localhost')
        HBNB_MYSQL_DB = getenv('hbnb_dev_db')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB,
                                             pool_pre_ping=True))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)


    def all(self, cls=None):
        """
        Return instance attributes
        Args:
            cls (obj): memory address of class
        Returns: 
            dictionary of objects
        """
        dbobjects = {}
        if cls:
            if type(cls) is str and cls in classes:
                for obj in self.__session.query(classes[cls]).all():
                    key = str(obj.__class__.__name__) + "." + str(obj.id)
                    val = obj
                    dbobjects[key] = val
            elif cls.__name__ in classes:
                 for obj in self.__session.query(cls).all():
                 key = str(obj.__class__.__name__) + "." + str(obj.id)
                    val = obj
                    dbobjects[key] = val
        else:
            for k, v in classes.items():
                for obj in self.__session.query(v).all():
                    key = str(v.__name__) + "." + str(obj.id)
                    val = obj
                    dbobjects[key] = val
        return dbobjects

    def new(self, obj):
        """
        add object to current database session
        Args:
            obj (obj): an object
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session obj if not None
        Args:
            obj (obj): an object
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database and the current database session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Call a private remove() session attribute""" 
        self.__session.remove()
