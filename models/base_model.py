#!/usr/bin/python3
"""Base Model module.

Contains BaseModel class which is
"base" of all other classes.
"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """Base Model module

    used for all common attributes and methods management for all other classes.

    Attributes:
        id (str): a uuid when an instance is created.
        created_at (datetime): the current datetime when an instance is created.
        updated_at (datetime): the current datetime when an instance is created and it will be updated.
    """

    def __init__(self, *args, **kwargs):
        """Initializes BaseModel.

        Args:
            *args: won’t be used.
            **kwargs (dict): dictionary.
        """
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()
        if kwargs is not None and kwargs != {}:
            for k, v in kwargs.items():
                if k in ["created_at", "updated_at"]:
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != "__class__":
                    setattr(self, k, v)
        else:
            models.storage.new(self)

    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance."""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
