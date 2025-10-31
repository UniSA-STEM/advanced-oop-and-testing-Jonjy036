'''
File: mammal.py
Description: the mammal child module (animal) for the advanced OOP and Testing Assignment.
Author: Jozef Jones
ID: 110484756
Username: jonjy036
This is my own work as defined by the University's Academic Integrity Policy.
'''
from abc import abstractmethod
from animal import Animal

class Mammal(Animal):
    def __init__(self, name, species, dob, gender, dietary_needs, is_mother):
        super().__init__(name, species, dob, gender, dietary_needs, is_mother)

    def eat(self):
        '''Standard eating behaviour by all classes (except where necessary).'''
        return f'{self.name} is eating. Munch munch.'

    # Make_sound remains abstract as sound is bespoke to individual species.
    @abstractmethod
    def make_sound(self):
        '''Animal Specific sound. this must be implemented by a child class'''
        pass

    def sleep(self):
        '''Standard sleeping behaviour by all classes (except where necessary).'''
        return f'Shhhhh. {self.name} is sleeping.'

    # New abstract method specific to mammals.
    @abstractmethod
    def nurse_young(self):
        '''Abstract nursing behaviour which is bespoke to mammals.'''
        pass

class Lion(Mammal):
    def make_sound(self):
        return 'ROOOAAAARRRRR!!!!'

    def nurse_young(self):
        if self.gender != 'female' or not self.is_mother:
            raise PermissionError(f'{self.name} cannot nurse any young.')
        return f'{self.name} is nursing young.'

class Chimpanzee(Mammal):
    def make_sound(self):
        return 'OOOHHH OOOHH AAHHHHHH AHHHHHHHH'

    def nurse_young(self):
        if self.gender != 'female' or not self.is_mother:
            raise PermissionError(f'{self.name} cannot nurse any young.')
        return f'{self.name} is nursing young.'

class Dingo(Mammal):
    def make_sound(self):
        return 'OOOOOOOHHHHHHHHHHOOOOO'

    def nurse_young(self):
        if self.gender != 'female' or not self.is_mother:
            raise PermissionError(f'{self.name} cannot nurse any young.')
        return f'{self.name} is nursing young.'