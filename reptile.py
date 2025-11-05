'''
File: animal.py
Description: the reptile child module (animal) for the advanced OOP and Testing Assignment.
Author: Jozef Jones
ID: 110484756
Username: jonjy036
This is my own work as defined by the University's Academic Integrity Policy.
'''
from animal import Animal
from abc import abstractmethod
from datetime import date
from species_data import *

class Reptile(Animal):
    def __init__(self, name, species, dob, gender, is_mother):
        super().__init__(name, species, dob, gender, is_mother)

    @property
    def environment_type(self):
        env = SPECIES_ENVIRONMENT.get(self.species.lower())
        if env is None:
            raise ValueError(f'there is novalid environment for a {self.species} listed.')
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

    def eat(self):
        '''Standard eating behaviour by all classes (except where necessary).'''
        return f'{self.name} is eating.'

    @abstractmethod
    # Make_sound remains abstract as sound is bespoke to individual species.
    def make_sound(self):
        '''Animal Specific sound. this must be implemented by a child class'''
        pass

    def sleep(self):
        '''Standard sleeping behaviour by all classes (except where necessary).'''
        return f'{self.name} is sleeping.'

    # Specific method for reptiles.
    def shed_skin(self):
        '''Shedding skin method which is bespoke to reptiles.'''
        return f'{self.name} has shed their skin, please tidy up.'

class Crocodile(Reptile):
    def __init__(self, name, dob, gender, is_mother=False):
        super().__init__(
            name = name,
            species = 'crocodile',
            dob = dob,
            gender = gender,
            is_mother = is_mother,
        )

    def make_sound(self):
        return '*gurgling* HHSSSSSSSSS'

class Python(Reptile):
    def __init__(self, name, dob, gender, is_mother=False):
        super().__init__(
            name=name,
            species='python',
            dob=dob,
            gender=gender,
            is_mother=is_mother,
        )

    def make_sound(self):
        return 'sssssssssssssssssssss'

class BeardedDragon(Reptile):
    def __init__(self, name, dob, gender, is_mother=False):
        super().__init__(
            name=name,
            species='bearded dragon',
            dob=dob,
            gender=gender,
            is_mother=is_mother,
        )

    def make_sound(self):
        return '*silence* \n\n(A bearded dragon does not make noise)'