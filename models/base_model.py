#!/usr/bin/env python3
"""BaseModel class"""
import uuid
from datetime import datetime
from dateutil import parser
from models import storage

class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """
        BaseModel constructor
        Args:
            id: random uuid from uuid module
            created_at: the date the object was created
            updated_at: the date the object was updated it will change
                        everytime the object got changed
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ("id",
                           "created_at",
                           "updated_at",
                           "__class__"):
                    continue
                setattr(self, key, value)
            self.id = kwargs["id"]
            self.created_at = parser.parse(kwargs["created_at"])
            self.updated_at = parser.parse(kwargs["updated_at"])

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        _dict = self.__dict__.copy()
        _dict["id"] = str(self.id)
        _dict["updated_at"] = self.updated_at.isoformat()
        _dict["created_at"] = self.created_at.isoformat()
        _dict["__class__"] = self.__class__.__name__
        return _dict

    def save(self):
        """
        updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime(
            datetime.now().year,
            datetime.now().month,
            datetime.now().day,
            datetime.now().hour,
            datetime.now().minute,
            datetime.now().second,
        )

    def __str__(self):
        """
        Overwrite the default behaviour of __str__ method
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
