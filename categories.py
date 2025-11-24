"""
File: categories.py
Description: This module represents the categories class. It is a parent class in which the categories
(child class) will inherit.
Author: Kim Xuyen Huynh
ID: 110442620
Username: Huykx001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal


class Mammal(Animal):
    """
    Mammal inherits attributes from the parent class (Animal).
    """

    def __init__(self, name, species, age, dietary, health_bar):
        # Invoke attributes from parent class.
        super().__init__(name, species, age, dietary, health_bar)
        self.__fur = "fur"  # unique trait.

    # Overriding Animal's abstract methods.
    def sound(self):
        # Function returns sound that the mammal makes.
        return f"{self.name} lets out a big growl"

    def eat(self):
        # Function displays the mammal eating.
        return f"{self.name} is tearing apart its prey!"

    def sleep(self):
        # Function displays the mammal sleeping.
        return f"{self.name} is currently sleeping! zzz"

    def __str__(self):
        return (f"\nI am {self.name} and a {self.species}\n"
                f"I am {self.age} years old and like {self.dietary}\n"
                f"I have {self.__fur}\n")


class Reptile(Animal):
    def __init__(self, name, species, age, dietary, health_bar):
        super().__init__(name, species, age, dietary, health_bar)
        self.__scale = "scales"  # unique trait.

    # Overriding Animal's abstract methods.
    def sound(self):
        try:
            # Function returns sound that reptile makes.
            print(f"{self.name} lets out a big hiss")
        except TypeError:
            print(f"Should be a string not int")

    def eat(self):
        # Function displays reptile eating.
        print(f"{self.name} is swallowing its food!")

    def sleep(self):
        # Function displays reptile sleeping.
        print(f"{self.name} is currently sleeping\n")

    def __str__(self):
        return (f"I am {self.name} and a {self.species}\n"
                f"I am {self.age} years old and like {self.dietary}\n"
                f"I have {self.__scale}\n")


class Bird(Animal):
    def __init__(self, name, species, age, dietary, health_bar):
        super().__init__(name, species, age, dietary, health_bar)
        self.__feather = "feathers"

    # Overriding Animal's abstract methods.
    def sound(self):
        # Function returns sound that the bird makes.
        print(f"{self.name} lets out a chirp!")

    def eat(self):
        # Function displays bird eating.
        print(f"{self.name} is pecking at its food!")

    def sleep(self):
        # Function displays bird sleeping.
        print(f"{self.name} is currently sleeping\n")

    def __str__(self):
        """
        Returns a sentence of the animal's information.
        """
        return (f"I am {self.name} and a {self.species}\n"
                f"I am {self.age} years old and like {self.dietary}\n"
                f"I have {self.__feather}\n")


class Fish(Animal):
    """
    Fish inherits attributes from the parent class (Animal).
    """

    def __init__(self, name, species, age, dietary, health_bar):
        super().__init__(name, species, age, dietary, health_bar)
        self.__gill = "gills"

    # Overriding Animal's abstract methods.
    def sound(self):
        # Function returns sound that reptile makes.
        print(f"{self.name} lets out a glub glub glub")

    def eat(self):
        # Function displays reptile eating.
        print(f"{self.name} is slurping its food!")

    def sleep(self):
        # Function displays reptile sleeping.
        print(f"{self.name} is currently sleeping\n")

    def __str__(self):
        return (f"I am {self.name} and a {self.species}\n"
                f"I am {self.age} years old and like {self.dietary}\n"
                f"I have {self.__gill}\n")
