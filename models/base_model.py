#!/usr/bin/python3
"""module for class BaseModel:
Define all common attributes / methods for other classes
"""


import json
import uuid
from datetime import datetime
import models


class BaseModel:
    """base class for unittest projects"""

    def __init__(self, *args, **kwargs):
        """class initialization"""
        isostr = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs and len(kwargs):
            for i, j in kwargs.items():
                if i != "__class__":
                    if i == "created_at":
                        self.created_at = datetime.strptime(j, isostr)
                    elif i == "updated_at":
                        self.updated_at = datetime.strptime(j, isostr)
                    else:
                        setattr(self, i, j)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """class initialization"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """update updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """return a dictionary copy of __dict__"""
        newdict = self.__dict__.copy()
        for keys, values in newdict.items():
            if type(values) is datetime:
                newdict[keys] = values.isoformat()
            else:
                newdict[keys] = values
        newdict["__class__"] = self.__class__.__name__
        return newdict
