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

from enclosure import Enclosure
from species_data import *

# Define Grandparent class of Animal.
class Animal(ABC):
    def __init__(self, name: str, species: str, dob: date, gender: str, is_mother: bool=False):

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

        if not isinstance(is_mother, bool):
            raise TypeError('is_mother must be a boolean')

        self.__name = name
        self.__species = species
        self.__dob = dob
        self.__gender = gender.lower()
        self.__is_mother = is_mother
        self.__enclosure = None

    def __str__(self):
        return (f'Name: {self.__name}\n'
                f'Species: {self.__species}\n'
                f'DOB: {self.__dob}\n'
                f'Gender: {self.__gender}\n'
                f'Is a mother: {self.__is_mother}\n'
                f'Required environment: {self.environment_type}\n'
                f'Enclosure size: {self.environment_size}\n'
                f'Enclosure: {self.__enclosure}\n'
                f'Dietary needs: {self.dietary_needs}\n\n')

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
    def is_mother(self):
        return self.__is_mother

    @is_mother.setter
    def is_mother(self, is_mother):
        if not isinstance(is_mother, bool):
            raise TypeError('is_mother must be a boolean')
        self.__is_mother = is_mother

    @property
    def environment_type(self):
        env = SPECIES_ENVIRONMENT.get(self.species.lower())
        if env is None:
            raise ValueError(f'there is no valid environment for a {self.species} listed.')
        return env

    @property
    def environment_size(self):
        size = ENVIRONMENT_SIZE.get(self.species.lower())
        if size is None:
            raise ValueError(f'No valid size listed for a {self.species}.')
        return size

    @property
    def dietary_needs(self):
        needs = SPECIES_DIETARY_NEEDS.get(self.species.lower())
        if needs is None:
            raise ValueError(f'No diet found for {self.species}.')
        return needs

    @property
    def enclosure(self):
        return self.__enclosure

    def eat(self, enclosure: Enclosure):
        if not self.enclosure:
            raise ValueError(f'{self.name} does not have an enclosure')
        if self.enclosure._food_level <= 0:
            return f'No food available in {self.enclosure.name}'
        self.enclosure._food_level -= 1
        return f'{self.name} ate some food from {self.enclosure.name}. There is {self.enclosure._food_level} food left.'

    # Define abstract methods to pass to children and grandchildren classes.
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def sleep(self):
        pass
