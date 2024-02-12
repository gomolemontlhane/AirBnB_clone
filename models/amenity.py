#!/usr/bin/python3
"""Defines the Amenity Modules/class.
Inherits from Superclass BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
