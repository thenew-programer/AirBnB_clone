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
        self.created_at = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f") 
        self.updated_at = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f") 



