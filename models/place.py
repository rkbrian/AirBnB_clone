#!/usr/bin/python3
"""
Module -- defines class ``Place``:
    inherits from class object ``BaseModel``
"""
from models.base_model import BaseModel
from datetime import datetime
import uuid


class State(BaseModel):
    """
    class object to define attributes/methods for each amenity of city
    """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_id = []

    def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__init__()
