#!/usr/bin/python3
"""File Storage Class.
Used for serialization into JSON file &
Used for deserializarion of JSON file into instances.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent a storage engine abstraction.

    Attributes:
        __file_path (str): The file name for saving objects.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of objects (__objects)."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with the key <obj_class_name>.id."""
        class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(class_name, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file __file_path (path is __file_path)."""
        objects_dict = FileStorage.__objects
        serialized_objects = {obj_key: obj.to_dict() for obj_key, obj in objects_dict.items()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file "__file_path" to __objects, given it exists."""
        try:
            with open(FileStorage.__file_path) as file:
                objects_dict = json.load(file)
                for obj_data in objects_dict.values():
                    class_name = obj_data["__class__"]
                    del obj_data["__class__"]
                    self.new(eval(class_name)(**obj_data))
        except FileNotFoundError:
            return
