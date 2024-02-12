#!/usr/bin/python3
"""Defines the State Module/Class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent a state.
    Inherits from BaseModel.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
