#!/usr/bin/python3
from models.base_model import BaseModel

""" User inherits BaseModel """


class User(BaseModel):
    """ User Class """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
