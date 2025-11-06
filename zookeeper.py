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
        return enclosure.clean_enclosure()

    def feed_animals(self, animals, enclosure: Enclosure):
        print(f'{self.name} is feeding the animals in {enclosure.name}')
        if not isinstance(animals, list):
            animals = [animals]

        for animal in animals:
            try:
                if animal is None:
                    print(f'No animal found for {animal}. moving to the next animal.')
                    continue

                result = animal.eat(enclosure)
                print(result)
            except Exception as e:
                animal_name = 'unknown'
                try:
                    animal_name = animal.name
                except AttributeError:
                    pass
                print(f'Error feeding {animal_name}: {e}')
