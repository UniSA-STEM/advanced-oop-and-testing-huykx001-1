"""
File: enclosure.py
Description: This module represents the enclosure class. It sorts out the animals into its
assigned enclosure.
Author: Kim Xuyen Huynh
ID: 110100110
Username: Huykx001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal
from categories import Mammal, Reptile, Bird, Fish
from staff import Staff


class Enclosure:
    """
    Constructor for the class Enclosure with private attributes such as
    size, environment, cleanliness level, and animals.
    """

    def __init__(self, size, environment_type, cleanliness_level):
        self.__size = size
        self.__environment_type = environment_type
        self.__cleanliness_level = cleanliness_level
        self.__animals = {"savannah": None,
                          "desert": None,
                          "forest": None,
                          "aquatic": None}

    # Getters for the private attribute animals.
    def get_animals(self):
        return self.__animals

    def get_cleanliness_level(self):
        return self.__cleanliness_level

    def get_environment_type(self):
        return self.__environment_type

    def check_compatibility(self, animal):
        """
        Function checks if the animal is suited for the habitat or not.
        """
        # checks if the type matches the specific habitat
        if self.__environment_type == "savannah":
            if isinstance(animal, Mammal):
                # Animal is compatible with habitat.
                return True
            else:
                # Animal is not compatible with habitat.
                print(f"{animal.get_name()} is not compatible with the savannah habitat.")
                return False

        if self.__environment_type == "desert":
            if isinstance(animal, Reptile):
                return True
            else:
                print(f"{animal.get_name()} is not compatible with the desert habitat.")
                return False

        if self.__environment_type == "forest":
            if isinstance(animal, Bird):
                return True
            else:
                print(f"{animal.get_name()} is not compatible with the forest habitat.")
                return False

        if self.__environment_type == "aquatic":
            if isinstance(animal, Fish):
                return True
            else:
                print(f"{animal.get_name()} is not compatible with the aquatic habitat.")
                return False

    def add_animal(self, habitat, animal):
        """
        Adds the animal into the specific enclosure.
        """
        # checks for compatibility
        if self.check_compatibility(animal):
            # Adds the animal into the enclosure if its empty.
            if self.__animals.get(habitat) == None:
                # Adds animal into the enclosure.
                self.__animals.update({habitat: animal.get_name()})
                print(f"Added {animal.get_name()} to the {self.__environment_type} enclosure.")

    def remove_animal(self, habitat, animal, vet=None):
        """
        Removes the animal from the specific enclosure.
        """
        # Cannot move animal if it is under treatment.
        if vet is not None:
            print(f"{animal.get_name()} is sick/or injured! they cannot be moved!")
        elif self.check_compatibility(animal):
            # No animal placed in a specific enclosure.
            if self.__animals.get(habitat) == None:
                print(f"There are currently no animals in the {self.__environment_type} enclosure.")
            else:
                # Animal is removed from the enclosure.
                self.__animals.update({habitat: (None)})
                print(f"removed {animal.get_name()} from the enclosure")

    # string conversion method to print the enclosure system.
    def __str__(self):
        """
        Returns the current status of animals in the system.
        """
        print(f"\n---{self.__environment_type.upper()} SYSTEM---")
        return "\n".join(f"{enclosure}: {animal}" for enclosure, animal in self.__animals.items())
