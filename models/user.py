#!/usr/bin/python3
"""User Model module.

Containing the User class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """defines a User.

    Attributes:
        email (str): user's email.
        password (str): user's password.
        first_name (str): user's first_name.
        last_name (str): user's last_name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
