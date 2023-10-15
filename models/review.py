#!/usr/bin/python3
"""Module to create a Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines the attributes for the review class"""
    place_id = ""
    user_id = ""
    text = ""
