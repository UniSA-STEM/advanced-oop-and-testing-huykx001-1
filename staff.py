"""
File: staff.py
Description: This module represents the staff's class. This module has a staff as the parent class
and the child class (vet and zookeeper) inheriting it.
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

    # getter for private attribute.
    def get_clean_percentage(self):
        return self.__clean_percentage

    def assign_enclosure(self, enclosure):
        """
        assigns the zookeeper to a specific enclosure
        """
        if enclosure.get_animals():
            # Assigns the zookeeper to the specific enclosure.
            self.get_assigned_enclosure().append(enclosure.get_environment_type())
            print(f"{self.get_name()} is now assigned to the {enclosure.get_environment_type()} enclosure.")
        else:
            # No animals assigned in an enclosure.
            print(f"There are currently no animals in the enclosure for {self.get_name()} to look after")

    def feed_animal(self, animal, hunger_level, current_hunger, enclosure):
        """
        feeds the animal depending on what level hunger it's at.
        """
        # Checks zookeeper is assigned to the enclosure.
        if enclosure.get_environment_type() in self.get_assigned_enclosure():
            # Animal cannot eat if it is already full.
            if animal.get_max_hunger() <= hunger_level:
                print(f"{animal.get_name()} is too full to consume more {animal.get_dietary()}!")
            else:
                # Animal consumes food, lowering its hunger level.
                hunger_level -= current_hunger
                print(f"{animal.get_name()} just consumed some delicious {animal.get_dietary()} yum!")
                print(f"Current hunger level: {current_hunger}")
        else:
            # Zookeeper is not assigned to any enclosures.
            print(f"{self.get_name()} is not assigned to any enclosures!")

    def clean_enclosure(self, enclosure):
        """
        cleans the enclosure depending on what cleanliness level it's at.
        """
        # Checks if Zookeeper is assigned to the enclosure.
        if enclosure.get_environment_type() in self.get_assigned_enclosure():
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
        else:
            # Zookeeper is not assigned to any enclosures.
            print(f"{self.get_name()} is not assigned to any enclosure")


class Veterinarian(Staff):
    """
    Constructor the child class inherited by the Staff class.
    """

    def __init__(self, name):
        super().__init__(name)
        self.__under_treatment = None
        self.__vet_enclosure = []

    # Getter for the private attribute.
    def get_under_treatment(self):
        return self.__under_treatment

    def assign_enclosure(self, enclosure):
        """
        Assigns vet to specific enclosure.
        """
        if enclosure.get_animals():
            # Assigns the Vet into the specific enclosure.
            self.__vet_enclosure.append(enclosure.get_environment_type())
            try:
                print(f"{self.get_name()} is now assigned to the {enclosure.get_environment_type()} enclosure")
            except TypeError:
                print("should be an string")

    def add_record(self, animal, record, enclosure):
        """
        record health issues added to the sick/injured animal.
        """
        # Checks if the vet is assigned to an enclosure.
        if enclosure.get_environment_type() in self.__vet_enclosure:
            print(f"{self.get_name()} has added the record {record.get_name()} to {animal.get_name()}")
            # Animal will now undergo treatment.
            self.__under_treatment = True
        else:
            # Vet is not assigned to any enclosures.
            print(f"{self.get_name()} cannot add record due to not being assigned to any enclosures!")

    def check_record(self):
        if self.__under_treatment:
            return f"under treatment!"
        else:
            return f"healthy!"

    def __str__(self):
        return (f"\n---HEATH STATUS---\n"
                f"name: Scar\n"
                f"status: {self.check_record()}")
