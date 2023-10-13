#!/usr/bin/env python3
"""Define Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class hold count of:

        city_id: it will be City.id
        user_id: it will be User.id
        name: the name of the posting I guess
        description: description of the posting
        number_rooms: number of rooms available
        number_bathrooms: number of bathrooms available 
        max_guest: max number of people that can enter the place
        price_by_night: price
        latitude: latitude of the place
        longitude: longitude of the place
        amenity_ids: t will be the list of Amenity.id later
    """

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
    amenity_ids = []
