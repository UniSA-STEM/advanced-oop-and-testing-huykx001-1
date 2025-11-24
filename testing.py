"""
File: testing.py
Description: This module represents the testing module. Its for testing the interacts if the classes to see
if it has passed or not.
Author: Kim Xuyen Huynh
ID: 110442620
Username: Huykx001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from categories import Mammal, Bird, Reptile, Fish
from enclosure import Enclosure
from staff import Staff, Zookeeper, Veterinarian
from systemHealthRecord import SystemHealthRecord
import pytest


# testing the category class.
class TestLion:

    @pytest.fixture
    def lion(self):
        return Mammal("Scar", "Lion", 40, "meat", 80)

    def test_attributes(self, lion):
        assert lion.get_name() == "Scar"
        assert lion.get_species() == "Lion"
        assert lion.get_age() == 40
        assert lion.get_health_bar() == 80

    # testing the methods.
    def test_sound(self, lion):
        assert lion.sound() == "Scar lets out a big growl"

    def test_eat(self, lion):
        assert lion.eat() == "Scar is tearing apart its prey!"

    def test_sleep(self, lion):
        assert lion.sleep() == "Scar is currently sleeping! zzz"


# testing the add/remove function.
class TestEnclosure:
    @pytest.fixture
    def lion(self):
        return Mammal("Scar", "Lion", 40, "meat", 80)

    @pytest.fixture
    def savannah(self):
        return Enclosure("large", "savannah", "dirty")

    # testing the methods.
    def test_add_animal(self, savannah, lion):
        savannah.add_animal(savannah, lion)
        # Checks if scar is in the system
        assert savannah.get_animals()[savannah] == "Scar"

    def test_remove_animal(self, savannah, lion):
        savannah.add_animal(savannah, lion)
        savannah.remove_animal(savannah, lion)
        # checks if scar is removed from the system
        assert savannah.get_animals()[savannah] is None


# testing the clean enclosure method
class TestZookeeper:
    @pytest.fixture
    def zoo(self):
        return Zookeeper("Raiden Shogun")

    @pytest.fixture
    def savannah(self):
        return Enclosure("large", "savannah", "dirty")

    # testing the method.
    def test_clean_enclosure(self, zoo, savannah):
        zoo.assign_enclosure(savannah)
        zoo.clean_enclosure(savannah)
        # clean percentage up by 50%
        assert zoo.get_clean_percentage() == 50


# testing vet adding health record to animal
class TestVeterinarian:
    @pytest.fixture
    def vet(self):
        return Veterinarian("Alice")

    @pytest.fixture
    def lion(self):
        return Mammal("Scar", "Lion", 40, "meat", 80)

    @pytest.fixture
    def savannah(self):
        return Enclosure("large", "savannah", "dirty")

    @pytest.fixture
    def fracture(self):
        return SystemHealthRecord("fracture", "20-11-25", "broken bone on the right leg", "most severe", "cast")

    # testing the method.
    def test_add_record(self, vet, lion, fracture, savannah):
        # adding the vet into enclosure
        vet.assign_enclosure(savannah)
        # adds health record onto the animal
        vet.add_record(lion, fracture, savannah)
        # confirms going under treatment
        assert vet.get_under_treatment() == True
