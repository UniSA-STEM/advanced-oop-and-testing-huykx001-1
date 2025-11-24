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

# do pytest and data validation

# testing the category class.
class TestLion:

    @pytest.fixture
    def lion(self):
        return Mammal("Scar", "Lion", 40, "meat", 80)

    def test_str(self, lion):
        assert lion.get_name() == "Scar"
        assert lion.get_species() == "Lion"
        assert lion.get_age() == 40
        assert lion.get_health_bar() == 80








