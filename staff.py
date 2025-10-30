'''
File: staff.py
Description: the staff module for the advanced OOP and Testing Assignment.
Author: Jozef Jones
ID: 110484756
Username: jonjy036
This is my own work as defined by the University's Academic Integrity Policy.
'''
from abc import ABC, abstractmethod

# Define Grandparent class of Animal.
class Animal(ABC):
    def __init__(self, name: str, species: str, age: int, dietary_needs: str):

        # Validate parameters.
        if not isinstance(name, str):
            raise TypeError('Name must be a string')
        elif not name:
            raise ValueError('Name cannot be empty')

        if not isinstance(species, str):
            raise TypeError('Species must be a string')
        elif not species:
            raise ValueError('Species cannot be empty')

        if not isinstance(age, int):
            raise TypeError('Age must be an integer')
        elif not age:
            raise ValueError('Age cannot be empty')

        if not isinstance(dietary_needs, str):
            raise TypeError('Dietary needs must be a string')
        elif not dietary_needs:
            raise ValueError('Dietary needs cannot be empty')

        self.__name = name
        self.__species = species
        self.__age = age
        self.__dietary_needs = dietary_needs

    # Define abstract methods to pass to children and grandchildren classes.
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

