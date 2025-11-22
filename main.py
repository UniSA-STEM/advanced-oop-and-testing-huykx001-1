"""
File: main.py
Description: A brief description of this Python module.
Author: Kim Xuyen Huynh
ID: 110442620
Username: Huykx001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal
from categories import Mammal, Reptile, Bird, Fish
from enclosure import Enclosure
from staff import Staff, Zookeeper, Veterinarian

# names for mammal, reptile, and bird
lion = Mammal("Scar", "Lion", 40, "meat")
chameleon = Reptile("Pascal", "Chameleon", 5, "insect")
northern_cardinal = Bird("Red", "Northern Cardinal", 20, "seed")
asian_carp = Fish("Magikarp", "Asian carp", 3, "plant")

# names for the enclosure
Savannah = Enclosure("large", "savannah", False)
Desert = Enclosure("small", "desert", True)
Forest = Enclosure("medium", "forest", True)
Aquatic = Enclosure("medium", "aquatic", True)

# testing here
# NOTE: tests are grouped under each comment. will only work if other groups are commented

# testing Mammal's methods and string conversion method
# lion.sound()
# lion.eat()
# lion.sleep()
# print(lion)

# testing Reptile's methods and string conversion method
# chameleon.sound()
# chameleon.eat()
# chameleon.sleep()
# print(chameleon)

# testing Bird's methods and string conversion method
# northern_cardinal.sound()
# northern_cardinal.eat()
# northern_cardinal.sleep()
# print(northern_cardinal)

# checking compatibility with habitat (working)
# Savannah.check_compatibility(lion)
# Desert.check_compatibility(chameleon)
# Forest.check_compatibility(northern_cardinal)
# Aquatic.check_compatibility(asian_carp)

# checking compatibility with habitat (not working)
# Savannah.check_compatibility(chameleon)
# Desert.check_compatibility(lion)
# Forest.check_compatibility(asian_carp)
# Aquatic.check_compatibility(northern_cardinal)

# adding animal to the enclosure
# Savannah.add_animal("savannah", lion)
# Desert.add_animal("desert", chameleon)
# Forest.add_animal("forest", northern_cardinal)
# Aquatic.add_animal("aquatic", asian_carp)
# Aquatic.add_animal("aquatic", lion) # is not compatible

# removing animal from the enclosure
Savannah.add_animal("savannah", lion)
Savannah.remove_animal("savannah", lion)
Savannah.remove_animal("savannah", lion) # no animal in enclosure