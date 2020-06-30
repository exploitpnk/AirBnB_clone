#!/usr/bin/python3
from models.base_model import BaseModel

""" Review inherits BaseModel """


class Review(BaseModel):
    """ Review Class """

    place_id = ""
    user_id = ""
    text = ""
