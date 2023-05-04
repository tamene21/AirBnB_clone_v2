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

    def all(self, cls=None):
        ''' Return a dict '''
        fs_objects = {}
        if cls:
            if type(cls) is str and cls in classes:
                for key, val in self.__objects.items():
                    if cls == key.split('.')[0]:
                        fs_objects[key] = val
            elif cls.__name__ in classes:
                for key, val in self.__objects.items():
                    if cls.__name__ == key.split('.')[0]:
                        fs_objects[key] = val
         else:
             return self.__objects
         return fs_objects

    def new(self, obj):
        ''' 
           set in objects the obj with key <obj class name>.id
           Arguments:
                obj : An instance object.
         '''
         key = str(obj.__class__.__name__) + "." + str(obj.id)
         value_dict = obj
         FileStorage.__objects[key] = value_dict

     def save(self):
         '''serializing to JSON file '''
         objects_dict = {}
         for key, val in FileStorage.__objects.items():
             objects_dict[key] = val.to_dict()
         with open(FileStorage.__file_path, mode='w', encoding='UTF8') as fd:
              json.dump(objects_dict, fd)

    def reload(self):
        '''JSON to __objects '''
        try:
            with open(FileStorage.__file_path, encoding='UTF8') as fd:
                FileStorage.__objects = json.load(fd)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        '''delete object if it is inside __objects '''
        if obj is not None:
            key = obj.__class__.name__ + "." + str(obj.id)
            if key in self.__objects:
                del self.__objects[key]
         self.save()


    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()
