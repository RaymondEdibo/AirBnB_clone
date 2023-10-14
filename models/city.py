#!/usr/bin/python3
"""City Model module.

Containing City class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """defines a City.

    Attributes:
        state_id (str): city's state id.
        name (str): city's name.
    """

    state_id = ""
    name = ""
