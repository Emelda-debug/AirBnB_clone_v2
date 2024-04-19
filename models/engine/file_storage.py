#!/usr/bin/python3
"""This module is the file storage class for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class FileStorage:
    """This class manages storage in json format
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns dictionary
        Return:
            returns dictionary of __object
        """
        dic = {}
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
                cls_dict = {}
                for x, y in self.__objects.items():
                    if type(y)== cls:
                        cls_dict[x] = y
                return cls_dict
            return self.__objects
    def new(self, obj):
        """adds new objects to given obj
        Args:
            obj: given object
        """
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Saves storage dictionary to file
        """
        odict = {o: self.__objects[o].to_dict() for o in
    self.__objects.keys()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(odict, f)

    def reload(self):
        """Loads storage dictionary from file
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for o in json.load(f).values():
                    name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(name)(**o))
        except FileNotFoundError:
            pass
        
    def delete(self, obj=None):
        """ deletes existing element
        """
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
            except (AttributeError, KeyError):
                pass

    def close(self):
        """ calls reload()
        """
        self.reload()
