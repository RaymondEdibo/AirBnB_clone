#!/usr/bin/python3
"""Place Model module.

Containing the Place class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """defines an Place.

    Attributes:
        city_id (str): city id.
        user_id (str): user id.
        name (str): name.
        description (str): description.
        number_rooms (int): number of rooms.
        number_bathrooms (int): number of bathrooms.
        max_guest (int): maximum number of guests.
        price_by_night (int): price by night.
        latitude (float): latitude.
        longitude (float): longitude.
        amenity_ids (list): list of amenities ids.
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
