'''
File: zoo_manager.py
Description: the ZooManager child module (Staff) for the advanced OOP and Testing Assignment.
Author: Jozef Jones
ID: 110484756
Username: jonjy036
This is my own work as defined by the University's Academic Integrity Policy.
'''
from staff import Staff
from enclosure import Enclosure


class ZooManager(Staff):
    def __init__(self, name, staff_number):
        super().__init__(name, staff_number)
        self._zookeeper_assignments = {}
        self._hospital_list = []

    @property
    def enclosure_list(self):
        return Enclosure.enclosure_list

    @property
    def zookeeper_assignments(self):
        return {zookeeper: list(enclosures) for zookeeper, enclosures in self._zookeeper_assignments.items()}

    @property
    def hospital_list(self):
        return self._hospital_list
    @hospital_list.setter
    def hospital_list(self, hospital_list):
        self._hospital_list = hospital_list

    def enclosure_report(self):
        if not Enclosure.enclosure_list:
            print('No enclosures available')
            return

        print('Enclosures Report:')
        for enclosure in Enclosure.enclosure_list:
            print(f'\nEnclosure {enclosure.name} is a {enclosure.size} {enclosure.environment} environment.')
            if enclosure.inhabitants:
                print('Animals: ')
                for animal in enclosure.inhabitants:
                    print(f'{animal.name} - {animal.species}')
                else:
                    print('No animals currently assigned to this enclosure.\n')

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

    def assign_zookeeper_to_enclosure(self, zookeeper, enclosure):
        if zookeeper is None or enclosure is None:
            raise AttributeError("Zookeeper and enclosure must be specified.")

        if zookeeper not in self._zookeeper_assignments:
            self._zookeeper_assignments[zookeeper] = []

        if enclosure not in self._zookeeper_assignments[zookeeper]:
            self._zookeeper_assignments[zookeeper].append(enclosure)
            print(f"Zookeeper {zookeeper.name} assigned to enclosure {enclosure.name}.")
        else:
            print(f"Zookeeper {zookeeper.name} is already assigned to enclosure {enclosure.name}.")

    def remove_zookeeper_assignment(self, zookeeper, enclosure):
        if zookeeper is None or enclosure is None:
            raise AttributeError("Zookeeper and enclosure must be specified.")

        if zookeeper in self._zookeeper_assignments:
            if enclosure in self._zookeeper_assignments[zookeeper]:
                self._zookeeper_assignments[zookeeper].remove(enclosure)
                print(f"Zookeeper {zookeeper.name} removed from {enclosure.name}.")
                if not self._zookeeper_assignments[zookeeper]:
                    del self._zookeeper_assignments[zookeeper]
                return True
            else:
                print(f"Zookeeper {zookeeper.name} was not assigned to {enclosure.name} so cannot be removed.")
                return False
        else:
            print(f"Zookeeper {zookeeper.name} has no enclosure assignments.")
            return False

    def get_enclosures_for_zookeeper(self, zookeeper):
        return self._zookeeper_assignments.get(zookeeper, [])

    def move_animal_to_hospital(self, animal):
        if animal.enclosure and animal in animal.enclosure.inhabitants:
            animal.original_enclosure = animal.enclosure
            self.remove_animal_from_enclosure(animal, animal.enclosure)
        if animal not in self.hospital_list:
            self.hospital_list.append(animal)
        animal.in_good_health = False

    def move_animal_out_of_hospital(self, animal):
        if animal in self.hospital_list:
            self.hospital_list.remove(animal)
        if hasattr(animal, 'original_enclosure') and animal.original_enclosure is not None:
            self.assign_animal_to_enclosure(animal, animal.original_enclosure)
        animal.in_good_health = True

    def add_enclosure(self, enclosure):
        if enclosure not in enclosure.enclosure_list:
            enclosure.enclosure_list.append(enclosure)