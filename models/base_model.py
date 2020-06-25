#!/usr/bin/python3

import uuid
import datetime


class BaseModel:
    """ Class base """
    def __init__(self, id=None, name=None, my_number=None, created_at=None, updated_at=None):
        """ ID setter """
        if id is not None:
            self.id = id
        else:
            self.id = str(uuid.uuid4())

        if name is not None:
            self.name = name
        if my_number is not None:
            self.my_number = my_number
        if created_at is not None:
            self.created_at = created_at
        else:
            self.created_at = datetime.datetime.now()
        if updated_at is not None:
            self.updated_at = updated_at
        else:
            self.updated_at = datetime.datetime.now()

    def created_at(self):
        self.created_at = datetime.datetime.now()

    def updated_at(self):
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """ __str__: string representation """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, str(self.__dict__))

    def save(self):
        """ save object to storage """
        self.updated_at = datetime.datetime.now()
        return self.updated_at
        #updated_at()
    def to_dict(self):
        """ to dict """
        return self.__dict__
