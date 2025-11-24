"""
File: testing.py
Description: A brief description of this Python module.
Author: Kim Xuyen Huynh
ID: 110442620
Username: Huykx001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from animal import Animal
from categories import Mammal, Bird, Reptile, Fish
from enclosure import Enclosure
from staff import Staff, Zookeeper, Veterinarian
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

    def test_add_animal(self, savannah, lion):
        savannah.add_animal(savannah, lion)
        # Checks if scar is in the system
        assert savannah.get_animals()[savannah] == "Scar"

    def test_remove_animal(self, savannah, lion):
        savannah.add_animal(savannah, lion)
        savannah.remove_animal(savannah, lion)
        # checks if scar is removed from the system
        assert savannah.get_animals()[savannah] is None

