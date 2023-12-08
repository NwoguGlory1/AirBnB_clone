#!/usr/bin/python3
"""Defines the module city"""


from models.base_model import BaseModel
from models.state import State
"""Defines the imported modules"""


class City(BaseModel):
    """Defines the child class City that inherits from the BaseModel class"""
    state_id = ""
    name = ""
