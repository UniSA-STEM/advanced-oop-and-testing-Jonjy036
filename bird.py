'''
File: mammal.py
Description: the bird child module (animal) for the advanced OOP and Testing Assignment.
Author: Jozef Jones
ID: 110484756
Username: jonjy036
This is my own work as defined by the University's Academic Integrity Policy.
'''
from animal import Animal
from abc import abstractmethod
from datetime import date

class Bird(Animal):
    def __init__(self, name, species, dob, gender, dietary_needs, is_mother):
        super().__init__(name, species, dob, gender, dietary_needs, is_mother)

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

    def fly(self):
        '''fly method which is bespoke to birds'''
        return f'{self.name} is flying. Flap Flap'

class Eagle(Bird):
    def __init__(self, name, dob, gender, is_mother=False):
        super().__init__(
            name=name,
            species='eagle',
            dob=dob,
            gender=gender,
            dietary_needs='rodents',
            is_mother=is_mother,
        )

    def make_sound(self):
        return 'Screeeecchh'

class Kookaburra(Bird):
    def __init__(self, name, dob, gender, is_mother=False):
        super().__init__(
            name=name,
            species='kookaburra',
            dob=dob,
            gender=gender,
            dietary_needs='insects & small rodents',
            is_mother=is_mother,
        )

    def make_sound(self):
        return 'hahahahahahaahahahahahahaha'

class Penguin(Bird):
    def __init__(self, name, dob, gender, is_mother=False):
        super().__init__(
            name=name,
            species='penguin',
            dob=dob,
            gender=gender,
            dietary_needs='fish',
            is_mother=is_mother,
        )

    def make_sound(self):
        return 'Hooonnnkkk'

    def fly(self):
        return f'{self.species}s cannot fly. They can swim though.'

    def swim(self):
        return f'{self.name} is swimming.'