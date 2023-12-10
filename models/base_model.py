#!/usr/bin/python3
"""This defines the BaseModel class."""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """This class represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """This initialize a new BaseModel.

        Args:
            *args (any): It is Unused.
            **kwargs (dict): This is the Key/value pairs of attributes.
        """
        tmform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tmform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """This Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """This Return the dictionary of the BaseModel instance.
        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """This Return the print/str representation of the BaseModel instance."""
        claname = self.__class__.__name__
        return "[{}] ({}) {}".format(claname, self.id, self.__dict__)
