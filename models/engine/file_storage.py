#!/usr/bin/python3
import datetime
import json


class FileStorage:
    """ Class to define the storage class
        Artributes:
            __file_path = contains the path to the file
            __objects = private atttribute to store the all objects
        Methods:
            all: return all the object in the __objects attributes
            new: add an new object to the __objects
            class: import all classes to be instanciated
            save: save all the object instances to a json file
            reload: load all the data from the file to __objects in the exit
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns all the objects in the __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """add a new object to __objects"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def classes(self):
        """contains all class to use for instanciating an object"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def save(self):
        """save the attribute of each instance to a file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            u = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(u, file)

    def reload(self):
        """ loads the attributes from from the file to and
            istantiate them into objects
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            for k, v in data.items():
                class_name, obj_id = k.split(".")
                cls = self.classes().get(class_name)
                if cls:
                    obj = cls(**v)
                    FileStorage.__objects[k] = obj
        except FileNotFoundError:
            return

    def attributes(self):
        """Returns the valid attributes and their types for classname"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
