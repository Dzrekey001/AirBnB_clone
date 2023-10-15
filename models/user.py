#!/usr/bin/python3
"""A class that defines the User"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class to define User attributes"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
