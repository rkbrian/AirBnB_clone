#!/usr/bin/python3
"""
Module -- defines class ``Amenity``:
    inherits from class object ``BaseModel``
"""
from models.base_model import BaseModel
from datetime import datetime
import uuid


class Amenity(BaseModel):
    """
    class object to define attributes/methods for each instance of amenity
    """
    name = ''

    def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__init__()
