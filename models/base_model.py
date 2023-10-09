#!/usr/bin/env python3
"""BaseModel class"""
import uuid
from datetime import datetime


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self):
        """
        BaseModel constructor
        Args:
            id: random uuid from uuid module
            created_at: the date the object was created
            updated_at: the date the object was updated it will change
                        everytime the object got changed
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime(
            datetime.now().year,
            datetime.now().month,
            datetime.now().day,
            datetime.now().hour,
            datetime.now().minute,
            datetime.now().second,
        )
        self.updated_at = datetime(
            datetime.now().year,
            datetime.now().month,
            datetime.now().day,
            datetime.now().hour,
            datetime.now().minute,
            datetime.now().second,
        )

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


s = BaseModel()
print(s)
