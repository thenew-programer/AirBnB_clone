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

    def __init__(self, *args, **kwargs):
        """constructor of the user class"""
        if not kwargs:
            super(User, self).__init__()
        else:
            super(User, self).__init__(**kwargs)
        storage.new(self)
