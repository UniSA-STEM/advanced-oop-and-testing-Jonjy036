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

class Reptile(Animal):
    SIZES = ['small', 'medium', 'large', 'extra large']
    def __init__(self, name, species, dob, gender, dietary_needs, is_mother, size: str):
        super().__init__(name, species, dob, gender, dietary_needs, is_mother)
        if not isinstance(size, str):
            raise TypeError('size must be a string')
        if size not in self.SIZES:
            raise ValueError(f'size must be one of {", ".join(self.SIZES)}')
        self.__size = size

    @property
    def size(self):
        return self.__size

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