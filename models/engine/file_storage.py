#!/usr/bin/python3

import json


class FileStorage:
    """class to define how object will be save and retrived"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            Description: Returns the dictionary __objects
            Return: __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
            Description:    Adds a new object to the __objects Dictionary

            Arguments:
                        obj(object): Object to be added to the dictionary

            Returns:    Always Nothing
        """
        obj_id = obj.id
        class_name = type(obj).__name__
        key = "{}.{}".format(class_name, obj_id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
            Description:
                        Serializes __objects to the
                        Json file(path: __file_path)
            Return:
                    Always Nothing
        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            obj_to_dict = {k: v.to_dict() for k, v
                           in FileStorage.__objects.items()}
            json.dump(obj_to_dict, file, indent=4)

    def classes(self):
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.review import Review
        from models.place import Place
        from models.state import State
        from models.user import User
        from models.city import City

        all_classes = {
                "BaseModel": BaseModel,
                "User": User,
                "Place": Place,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Review": Review
                }
        return all_classes

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                json_data = json.load(file)

                for key, value in json_data.items():
                    class_name, obj_id = key.split(".")
                    cls = self.classes().get(class_name)

                    if cls:
                        obj = cls(**value)
                        FileStorage.__objects[key] = obj
        except FileNotFoundError:
            return
