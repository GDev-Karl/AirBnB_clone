#!/usr/bin/python3

import uuid
from datetime import datetime
from models import storage

"""
    This import the datetime modules to get the date
"""


class BaseModel:
    """This BaseModel class will serve as the base for other classes"""
    def __init__(self, *args, **kwargs):
        """
           The __init__ method initializes instances of the class
        """
        if kwargs:
            if "__class__" in kwargs:
                del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """This returns a representation of the object"""
        return f"[{self.__class__.__name__}] ({getattr(self, 'id', None)}) {self.__dict__}"

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def save(self):
        storage.new(self)
        storage.save()
