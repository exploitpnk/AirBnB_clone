#!/usr/bin/python3

import uuid
import datetime
from models import storage

class BaseModel:
    """ Class base """
    def __init__(self, *args, **kwargs):
        if kwargs != {}:
            if kwargs["id"] is not None:
                self.id = kwargs["id"]
            if kwargs["created_at"] is not None:
                self.created_at = datetime.datetime.fromisoformat(kwargs["created_at"])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        storage.new(self)

    def __str__(self):
        """ __str__: string representation """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, str(self.__dict__))

    def save(self):
        """ save object to storage """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """ to dict """
        ret = self.__dict__.copy()
        ret["__class__"] = self.__class__.__name__
        ret["updated_at"] = self.updated_at.isoformat()
        ret["created_at"] = self.created_at.isoformat()
        return ret
