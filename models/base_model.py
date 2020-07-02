#!/usr/bin/python3

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """ Class base """
    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            if key == '__class__':
                continue
            if key == 'updated_at':
                val = datetime.fromisoformat(kwargs["updated_at"])
            if key == 'created_at':
                val = datetime.fromisoformat(kwargs["created_at"])
            setattr(self, key, val)
        if 'id' not in kwargs.keys():
            self.id = str(uuid.uuid4())
        if 'created_at' not in kwargs.keys():
            self.created_at = datetime.now()
        if 'updated_at' not in kwargs.keys():
            self.updated_at = datetime.now()
        if len(kwargs) == 0:
            storage.new(self)

    def __str__(self):
        """ __str__: string representation """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     str(self.__dict__))

    def save(self):
        """ save object to storage """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ to dict """
        ret = self.__dict__.copy()
        ret["__class__"] = self.__class__.__name__
        ret["updated_at"] = self.updated_at.isoformat()
        ret["created_at"] = self.created_at.isoformat()
        return ret
