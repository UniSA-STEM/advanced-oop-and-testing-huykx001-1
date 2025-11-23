"""
File: staff.py
Description: A brief description of this Python module.
Author: Kim Xuyen Huynh
ID: 110442620
Username: Huykx001
This is my own work as defined by the University's Academic Integrity Policy.
"""

# Note: remember to add data validation, testing

class Staff:
    """
    Constructor for the class Staff with private attributes such as
    name,assigned_animals, and assigned enclosure.
    """

    def __init__(self, name):
        self.__name = name
        self.__assigned_enclosure = []

    # Getters for the private attributes.
    def get_name(self):
        return self.__name

    def get_assigned_enclosure(self):
        return self.__assigned_enclosure

    def assign_enclosure(self, enclosure):
        pass


class Zookeeper(Staff):
    """
    Constructor the child class inherited by the Staff class.
    """

    def __init__(self, name):
        super().__init__(name)

    def assign_enclosure(self, enclosure):
        """
        assigns the zookeeper to a specific enclosure
        """
        self.get_assigned_enclosure().append(enclosure)
        print(f"{self.get_name()} is now assigned to the enclosure.")


class Veterinarian(Staff):
    """
    Constructor the child class inherited by the Staff class.
    """

    def __init__(self, name):
        super().__init__(name)
