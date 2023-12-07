#!/usr/bin/python3
"""Defines the module review"""


from models.base_model import BaseModel
from models.place import Place
from models.user import User
"""Defines the imported modules"""


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
