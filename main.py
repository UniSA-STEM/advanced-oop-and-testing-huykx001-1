"""
File: main.py
Description: A brief description of this Python module.
Author: Kim Xuyen Huynh
ID: 110442620
Username: Huykx001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal
from categories import Mammal, Reptile, Bird
from staff import Staff, Zookeeper, Veterinarian

# names for mammal, reptile, and bird
mammal = Mammal("Scar", "Lion", 40, "meat")
reptile = Reptile("Pascal", "Chameleon", 5, "insect")
bird = Bird("Red", "Northern Cardinal", 20, "seed")

# testing here
# NOTE: tests are grouped under each comment. will only work if other groups are commented

# testing Mammal's methods and string conversion method
mammal.sound()
mammal.eat()
mammal.sleep()
print(mammal)

# testing Reptile's methods and string conversion method
reptile.sound()
reptile.eat()
reptile.sleep()
print(reptile)

# testing Bird's methods and string conversion method
bird.sound()
bird.eat()
bird.sleep()
print(bird)

