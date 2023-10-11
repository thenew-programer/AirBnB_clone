#!/usr/bin/env python3
"""Define User class"""
from models import storage
from models.base_model import BaseModel


class User(BaseModel):
    """ class User that inherits from BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self):
        """constructor of the user class"""
        super(User, self).__init__()
