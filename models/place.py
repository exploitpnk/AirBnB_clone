#!/usr/bin/python3
from models.base_model import BaseModel

""" Place inherits BaseModel """


class Place(BaseModel):
    """ Place Class """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_room = ""
    number_bathrooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = 0.0
    longitude = 0.0
    amenty_ids = []
