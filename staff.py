"""
File: staff.py
Description: A brief description of this Python module.
Author: Kim Xuyen Huynh
ID: 110442620
Username: Huykx001
This is my own work as defined by the University's Academic Integrity Policy.
"""

class Staff:
    """
    Constructor for the class Staff with private attributes such as
    name,assigned_animals, and assigned enclosure.
    """
    def __init__(self, name):
        self.__name = name
        self.__assigned_animals = []
        self.__assigned_enclosure = []

class Zookeeper(Staff):
    """
    Constructor the child class inherited by the Staff class.
    """
    def __init__(self, name, assigned_animals, assigned_enclosure):
        super().__init__(name, assigned_animals, assigned_enclosure)

class Veterinarian(Staff):
    """
    Constructor the child class inherited by the Staff class.
    """
    def __init__(self, name, assigned_animals, assigned_enclosure):
        super().__init__(name, assigned_animals, assigned_enclosure)


