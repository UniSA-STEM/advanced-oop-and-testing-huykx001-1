"""
File: enclosure.py
Description: This module represents the enclosure class.
Author: Kim Xuyen Huynh
ID: 110100110
Username: Huykx001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal
from categories import Mammal, Reptile, Bird


class Enclosure:
    """
    Constructor for the class Enclosure with private attributes such as
    size, environment, cleanliness level, and animals.
    """

    def __init__(self, size, environment_type, cleanliness_level):
        self.__size = size
        self.__environment_type = {"Savannah": None,
                                   "Desert": None,
                                   "Forest": None,
                                   "Aquatic": None}
        self.__cleanliness_level = cleanliness_level
        self.__animals = []

    def get_environment_type(self):
        pass

    def add_animal(self, animal):
        pass

    def remove_animal(self, animal):
        pass

    def __str__(self):
        """
        returns the current status
        """
        pass
