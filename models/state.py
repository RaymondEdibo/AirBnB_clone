#!/usr/bin/python3
"""State Model module.

Containing the State class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """defines a State.

    Attributes:
        name (str): state's name.
    """

    name = ""
