#!/usr/bin/python3
"""Amenity Model module.

Containing the Amenity class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """defines an Amenity.

    Attributes:
        name (str): amenity's name.
    """

    name = ""
