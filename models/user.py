#!/usr/bin/python3
"""
Module -- defines class ``User``:
    inherits from class object ``BaseModel`` and,
    manages all other instances of new User
"""
from models.base_model import BaseModel
from datetime import datetime
import uuid


class User(BaseModel):
    """
    class object to define attributes/method of each instance of user
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__init__()
