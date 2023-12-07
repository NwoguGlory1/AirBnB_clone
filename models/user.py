#!/usr/bin/python3
"""Defines the module user"""


from models.base_model import BaseModel
"""Defines the imported modules"""


class User(BaseModel):
    """Defines the child class user that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
