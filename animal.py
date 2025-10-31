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
    def __init__(self, name: str, species: str, dob: date, gender: str, dietary_needs: str, is_mother: bool=False):

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
            raise TypeError('DOB must be a date')
        elif not dob:
            raise ValueError('DOB cannot be empty')

        if not isinstance(gender, str):
            raise TypeError('Gender must be a string')
        elif not gender:
            raise ValueError('Gender cannot be empty')
        allowed_genders = ['male', 'female']
        if gender.lower() not in allowed_genders:
            raise ValueError('Gender must be "male" or "female"')

        if not isinstance(dietary_needs, str):
            raise TypeError('Dietary needs must be a string')
        elif not dietary_needs:
            raise ValueError('Dietary needs cannot be empty')

        if not isinstance(is_mother, bool):
            raise TypeError('is_mother must be a boolean')

        self.__name = name
        self.__species = species
        self.__dob = dob
        self.__gender = gender.lower()
        self.__dietary_needs = dietary_needs
        self.__is_mother = is_mother

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
    def gender(self):
        return self.__gender

    @property
    def dietary_needs(self):
        return self.__dietary_needs

    @property
    def is_mother(self):
        return self.__is_mother

    @dietary_needs.setter
    def dietary_needs(self, dietary_needs):
        if not isinstance(dietary_needs, str):
            raise TypeError('Dietary needs must be a string')
        elif not dietary_needs:
            raise ValueError('Dietary needs cannot be empty')
        self.__dietary_needs = dietary_needs

    @is_mother.setter
    def is_mother(self, is_mother):
        if not isinstance(is_mother, bool):
            raise TypeError('is_mother must be a boolean')
        self.__is_mother = is_mother

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
