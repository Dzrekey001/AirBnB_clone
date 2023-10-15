#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:

    def __init__(self, *args, **kwargs):
        """
            Description:    generate a unique id, create and update
                            the time the class was created.
                            This will apply to all classes inheriting from
                            this class.
            Attribute:
                    created_at (datetime):  set the time the class
                                            was instantiated.
                    updated_at (datetime):  set the time the class was updated
                    id (str): gives a unique identity to each class instance.
            Arguments:
                    *args (None): wont be used
                    **kwargs (dict): should contains attribute names and values
        """
        if kwargs:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs["id"]
                elif key == "created_at":
                    c_date = datetime.fromisoformat(kwargs["created_at"])
                    self.created_at = c_date
                elif key == "updated_at":
                    u_date = datetime.fromisoformat(kwargs["updated_at"])
                    self.updated_at = u_date
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
            Description:    returns how the class should be printed
            Usage:
                >>>print(str(<class_instance>))
        """
        cls_name = type(self).__name__
        cls_dict = self.__dict__
        str_rep = "[{}] ({}) {}".format(cls_name, self.id, cls_dict)
        return str_rep

    def save(self):
        """
            Description:
                        saves anything that needs to be updated of call
                        all save functions
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Description:
                    Returns the dictionary representation of
                    the class instance with class instance attributes.
        """
        dictionary = self.__dict__.copy()
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["__class__"] = type(self).__name__
        return dictionary
