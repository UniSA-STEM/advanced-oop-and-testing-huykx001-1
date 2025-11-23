"""
File: staff.py
Description: A brief description of this Python module.
Author: Kim Xuyen Huynh
ID: 110442620
Username: Huykx001
This is my own work as defined by the University's Academic Integrity Policy.
"""

# Note: remember to add data validation, testing

from categories import Mammal, Reptile, Bird, Fish
from systemHealthRecord import SystemHealthRecord


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
        self.__clean_percentage = 0

    def assign_enclosure(self, enclosure):
        """
        assigns the zookeeper to a specific enclosure
        """
        self.get_assigned_enclosure().append(enclosure)
        print(f"{self.get_name()} is now assigned to the enclosure.")

    def feed_animal(self, animal, hunger_level, current_hunger):
        """
        feeds the animal depending on what level hunger it's at.
        """
        # Animal cannot eat if it is already full.
        if animal.get_max_hunger() <= hunger_level:
            print(f"{animal.get_name()} is too full to consume more {animal.get_dietary()}!")
        else:
            # Animal consumes food, lowering its hunger level.
            hunger_level -= current_hunger
            print(f"{animal.get_name()} just consumed some delicious {animal.get_dietary()} yum!")
            print(f"Current hunger level: {current_hunger}")

    def clean_enclosure(self, enclosure):
        """
        cleans the enclosure depending on what cleanliness level it's at.
        """
        # The enclosure is now untidy.
        if enclosure.get_cleanliness_level() == "dirty":
            self.__clean_percentage += 50
            print(f"cleaning enclosure...cleanliness now is at {self.__clean_percentage}%")
        # The enclosure is now fully cleaned.
        elif enclosure.get_cleanliness_level() == "untidy":
            self.__clean_percentage += 100
            print(f"cleaning enclosure...cleanliness now is at {self.__clean_percentage}% fully cleaned!")
        elif enclosure.get_cleanliness_level() == "clean":
            print(f"The enclosure is already cleaned!")


class Veterinarian(Staff):
    """
    Constructor the child class inherited by the Staff class.
    """
    def __init__(self, name):
        super().__init__(name)
        self.__under_treatment = False

    # Getter for the private attribute.
    def get_under_treatment(self):
        return self.__under_treatment

    def add_record(self, animal, record):
        """
        record health issues added to the sick/injured animal.
        """
        print(f"Added the record {record.get_name()} to the {animal.get_name()}")
        self.__under_treatment = True

