"""
File: animal.py
Description: This module represents the Animal abstract class. It contains
various method methods and a string conversion to print a message.
Author: Kim Xuyen Huynh
ID: 110442620
Username: Huykx001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, species, age, dietary):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__dietary = dietary

    # Getters for the private attributes.
    def get_name(self):
        return self.__name

    def get_species(self):
        return self.__species

    def get_age(self):
        return self.__age

    def get_dietary(self):
        return self.__dietary

    # Placeholders for the Animal class.
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    # properties
    name = property(get_name)
    species = property(get_species)
    age = property(get_age)
    dietary = property(get_dietary)

    def __str__(self):
        return (f"name: {self.__name}\n"
                f"species: {self.__species}\n"
                f"age: {self.__age}\n"
                f"dietary: {self.__dietary}")
