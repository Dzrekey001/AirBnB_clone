#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """ Base clase for the AirBnB project
        func:
            __int__: initialize the object
            __str__: return the string representation of the BassModel
                    as [<class name>] (<self.id>) <self.__dict__>
            save:   update the date to the day changes were made
            to_dict:    create a dictionary of all attributes in the BaseModel
    """

    def __init__(self, *args, **kwargs):
        """Initializes the BaseModel with attribues and values
        params:
                *args: values passed to the BaseModel saved as tuple
                **kwargs: key/value passes to the BaseModel
        Attributes:
                created_at: time the an instance was created
                updated_at: time the instance is updated
                id: unique ID generated for each instance
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], f"%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], f"%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return the string representation of the BaseModel Class"""
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the time the instance was modified"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary of all the attributes in the class"""
        base_dict = self.__dict__.copy()
        base_dict["__class__"] = type(self).__name__
        base_dict["created_at"] = base_dict["created_at"].isoformat()
        base_dict["updated_at"] = base_dict["updated_at"].isoformat()
        return base_dict
