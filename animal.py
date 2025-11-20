"""
File: filename.py
Description: This module represents the Animal abstract class. It contains
various method methods and a string conversion to print a message.
Author: Kim Xuyen Huynh
ID: 110442620
Username: Huykx001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    def __int__(self, name, species, age, dietary):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__dietary = dietary

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    def __str__(self):
        return (f"name: {self.__name}\n"
                f"species: {self.__species}\n"
                f"age: {self.__age}\n"
                f"dietary: {self.__dietary}")
