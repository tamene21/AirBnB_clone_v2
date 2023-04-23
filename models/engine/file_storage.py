#!/usr/bin/python3
"""
containes the FileStorage class
"""

import json
from models.amenity import Amenity
from model.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity":Amenity, "BaseModel": BaseModel, "City": City, "place": Place,
          "Review":Review, "State": State, "User": User}


class FileStorage:
    """serializes instances to JSON file and deserializes to to instances"""
    _file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()
