"""
File: main.py
Description: This module represents the main module. It is for testing the classes to see how they
interact with each other.
Author: Kim Xuyen Huynh
ID: 110442620
Username: Huykx001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal
from categories import Mammal, Reptile, Bird, Fish
from enclosure import Enclosure
from staff import Staff, Zookeeper, Veterinarian
from systemHealthRecord import SystemHealthRecord

# names for mammal, reptile, and bird
lion = Mammal("Scar", "Lion", 40, "meat", 80)
chameleon = Reptile("Pascal", "Chameleon", 5, "insect", 70)
northern_cardinal = Bird("Red", "Northern Cardinal", 20, "seed", 100)
asian_carp = Fish("Magikarp", "Asian carp", 3, "plant", 20)

# names for the enclosure
Savannah = Enclosure("large", "savannah", "dirty")
Desert = Enclosure("small", "desert", "untidy")
Forest = Enclosure("medium", "forest", "clean")
Aquatic = Enclosure("medium", "aquatic", "clean")

# names for staffs
zoo = Zookeeper("Raiden Shogun")
vet = Veterinarian("Alice")

# records from the health system
fracture = SystemHealthRecord("fracture", "20-11-25", "broken bone on the right leg", "most severe", "cast")
flu = SystemHealthRecord("flu", "21-11-25", "common cold", "less severe", "antibiotics")

# testing here
# NOTE: tests are grouped under each comment. will only work if other groups are commented

# testing Mammal's methods and string conversion method
print(lion.sound())
print(lion.eat())
print(lion.sleep())
print(lion)

# testing Reptile's methods and string conversion method
chameleon.sound()
chameleon.eat()
chameleon.sleep()
print(chameleon)

# testing Bird's methods and string conversion method
northern_cardinal.sound()
northern_cardinal.eat()
northern_cardinal.sleep()
print(northern_cardinal)

# testing Fish's methods and string conversion method
asian_carp.sound()
asian_carp.eat()
asian_carp.sleep()
print(asian_carp)

# adding animal to the enclosure
Savannah.add_animal("savannah", lion)
Desert.add_animal("desert", chameleon)
Forest.add_animal("forest", northern_cardinal)
Aquatic.add_animal("aquatic", asian_carp)
Aquatic.add_animal("aquatic", lion)  # is not compatible
print(Savannah)
print(Desert)
print(Forest)
print(Aquatic)

# removing animal from the enclosure
Savannah.add_animal("savannah", lion)
Savannah.remove_animal("savannah", lion)
Savannah.remove_animal("savannah", lion)  # no animal in enclosure
print(Savannah)

# assigning zookeeper and cleaning enclosure.
Savannah.add_animal("savannah", lion)
zoo.assign_enclosure(Savannah)  # cannot clean if zookeeper is not assigned to enclosure
zoo.clean_enclosure(Savannah)

# assigning zookeeper and feeding the animal
Savannah.add_animal("savannah", lion)
zoo.assign_enclosure(Savannah)  # cannot clean if zookeeper is not assigned to enclosure
zoo.feed_animal(lion, 60, 50, Savannah)
zoo.feed_animal(lion, 100, 100, Savannah)  # too full to consume meal

# cannot remove animal when sick/or injured
vet.assign_enclosure(Savannah)
Savannah.add_animal("savannah", lion)
vet.add_record(lion, fracture, Savannah)
Savannah.remove_animal("savannah", lion, vet)
print(vet)
print(fracture)
