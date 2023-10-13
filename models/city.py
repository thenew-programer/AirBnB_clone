#!/usr/bin/env python3
"""Define City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class that will hold count of the city"""
    state_id = ""
    name = ""
