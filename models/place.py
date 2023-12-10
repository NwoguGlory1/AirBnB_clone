#!/usr/bin/python3
"""Defines the module place"""


from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
"""Defines the imported modules"""


class Place(BaseModel):
    """Defines the child class Place that inherits from the class BaseModel"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = [""]
