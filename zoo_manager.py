'''
File: zoo_manager.py
Description: the ZooManager child module (Staff) for the advanced OOP and Testing Assignment.
Author: Jozef Jones
ID: 110484756
Username: jonjy036
This is my own work as defined by the University's Academic Integrity Policy.
'''
from staff import Staff
from animal import Animal
from enclosure import Enclosure


class ZooManager(Staff):
    def __init__(self, name, staff_number):
        super().__init__(name, staff_number)

    def assign_animal_to_enclosure(self, animal, enclosure):
        if animal is None:
            raise AttributeError(f'There is no record of {animal} at the zoo.')
        if enclosure is None:
            raise AttributeError(f'There is no record of {enclosure} at the zoo.')
        if not enclosure.appropriate_species(animal):
           print(f'{animal} was not assigned to the enclosure')
           return False

        if animal not in enclosure.inhabitants:
            enclosure.inhabitants.append(animal)
            animal.enclosure = enclosure
            print(f'{self.name} assigned {animal.name} to {enclosure.name}.')
            return True
        else:
            print(f'{animal.name} is already in {enclosure.name}.')
            return False

    def remove_animal_from_enclosure(self, animal, enclosure):
        if animal is None:
            raise AttributeError(f'There is no record of {animal} at the zoo.')
        if enclosure is None:
            raise AttributeError(f'There is no record of {enclosure} at the zoo.')

        if animal in enclosure.inhabitants:
            enclosure.inhabitants.remove(animal)
            animal.enclosure = None
            print(f'{self.name} removed {animal.name} from the enclosure {enclosure.name}')
            if not enclosure.inhabitants:
                enclosure.species_in_enclosure = None
                print(f'Enclosure {enclosure.name} is now empty.')
            return True
        else:
            print(f'{animal.name} was not found in enclosure {enclosure.name}. No animals have been removed.')
            return False
