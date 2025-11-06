'''
File: zookeeper.py
Description: the zookeeper child module (staff) for the advanced OOP and Testing Assignment.
Author: Jozef Jones
ID: 110484756
Username: jonjy036
This is my own work as defined by the University's Academic Integrity Policy.
'''
from staff import Staff
from enclosure import Enclosure

class Zookeeper(Staff):
    def __init__(self, name, staff_number):
        super().__init__(name, staff_number)

    def clean_enclosure(self, enclosure):
        if enclosure is None:
            raise ValueError(f'{enclosure} is not a valid enclosure')
        print(f'{self.name} cleaning enclosure {enclosure.name}')
        enclosure.cleanliness = 100

    def feed_animals(self, animals, enclosure: Enclosure):
        if enclosure is None:
            raise ValueError(f'{enclosure} is not a valid enclosure')

        num_animals = len(enclosure.inhabitants)
        if num_animals == 0:
            print(f'There are no animals in {enclosure.name}.')
            return

        enclosure._food_level += num_animals

        print(f'{self.name} has added {num_animals} portions of food to {enclosure.name}.')
