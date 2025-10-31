'''
File: animal.py
Description: the animal module for the advanced OOP and Testing Assignment.
Author: Jozef Jones
ID: 110484756
Username: jonjy036
This is my own work as defined by the University's Academic Integrity Policy.
'''
from abc import ABC, abstractmethod
from datetime import date

# Define Grandparent class of Animal.
class Animal(ABC):
    def __init__(self, name: str, species: str, dob: date, dietary_needs: str):

        # Validate parameters.
        if not isinstance(name, str):
            raise TypeError('Name must be a string')
        elif not name:
            raise ValueError('Name cannot be empty')

        if not isinstance(species, str):
            raise TypeError('Species must be a string')
        elif not species:
            raise ValueError('Species cannot be empty')

        if not isinstance(dob, date):
            raise TypeError('Age must be a date')
        elif not dob:
            raise ValueError('DOB cannot be empty')

        if not isinstance(dietary_needs, str):
            raise TypeError('Dietary needs must be a string')
        elif not dietary_needs:
            raise ValueError('Dietary needs cannot be empty')

        self.__name = name
        self.__species = species
        self.__dob = dob
        self.__dietary_needs = dietary_needs

    # Add property decorators for getters and setters.
    @property
    def name(self):
        return self.__name

    @property
    def species(self):
        return self.__species

    @property
    def age(self):
        today = date.today()
        years = today.year - self.__dob.year
        if (today.month, today.day) < (self.__dob.month, self.__dob.day):
            years -= 1
        return f'{years} years old'

    @property
    def dietary_needs(self):
        return self.__dietary_needs

    @dietary_needs.setter
    def dietary_needs(self, dietary_needs):
        if not isinstance(dietary_needs, str):
            raise TypeError('Dietary needs must be a string')
        elif not dietary_needs:
            raise ValueError('Dietary needs cannot be empty')
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
