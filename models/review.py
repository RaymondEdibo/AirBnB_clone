#!/usr/bin/python3
"""Review Model module.

Containing the Review class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """defines a Review.

    Attributes:
        place_id (str): place id.
        user_id (str): issuer user id.
        text (str): the review
    """

    place_id = ""
    user_id = ""
    text = ""
