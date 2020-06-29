#!/usr/bin/python3
""" engine of the json data base """
import json


class FileStorage:
    """ File storage Engine Class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return all storage objs """
        return FileStorage.__objects

    def new(self, obj):
        id_obj = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[id_obj] = obj

    def save(self):
        json_d = {}
        for key, val in FileStorage.__objects.items():
            json_d[key] = val.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as coso:
            json.dump(json_d, coso)

    def reload(self):
        try:
            with open(FileStorage.__file_path, encoding="utf-8") as coso:
                from models.base_model import BaseModel

                chrge = json.load(coso)
                for key, val in chrge.items():
                    cl = val["__class__"]
                    ob = eval(cl + "(**val)")
                    FileStorage.__objects[key] = ob
        except IOError:
            pass
