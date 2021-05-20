#!/usr/bin/python3
"""
Module -- defines class ``State``:
    inherits from class object ``BaseModel``
"""
from models.base_model import BaseModel
from datetime import datetime
import uuid


class State(BaseModel):
    """
    class object to define attributes/methods for each instance of state
    """
    name = ''

    def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__init__()
