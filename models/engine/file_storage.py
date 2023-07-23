#!/usr/bin/python3
"""-*- coding: utf-8 -*-"""

import json


class FileStorage:
    """Serializes and deserializes JSON file"""

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            obj_dict = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects(only if the file exists)"""
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    class_name = eval(class_name)
                    self.__objects[key] = class_name(**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects.pop(key, None)

    def close(self):
        """Calls reload() method for deserializing the JSON file to objects"""
        self.reload()
