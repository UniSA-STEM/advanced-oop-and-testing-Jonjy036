'''
File: enclosure.py
Description: the enclosure module for the advanced OOP and Testing Assignment.
Author: Jozef Jones
ID: 110484756
Username: jonjy036
This is my own work as defined by the University's Academic Integrity Policy.
'''
from species_data import ENVIRONMENT_SIZE


class Enclosure:
    ALLOWED_SIZES = ['extra small', 'small', 'medium', 'large', 'extra large']

    def __init__(self, name: str, size, environment, cleanliness=100):
        self.__name = name
        if size not in Enclosure.ALLOWED_SIZES:
            raise ValueError('The size of the enclosure must be one of the allowed sizes')
        self.__size = size
        self.__environment = environment
        self.__cleanliness = cleanliness
        self.__inhabitants = []
        self.__species_in_enclosure = None
        self._food_level = 0

    def __str__(self):
        inhabitants_string = '\n'.join(str(animal) for animal in self.__inhabitants) if self.__inhabitants else 'No inhabitants'
        return (f'Enclosure: {self.__name}\n'
                f'Size: {self.__size}\n'
                f'Environment: {self.__environment}\n'
                f'Cleanliness: {self.__cleanliness}\n'
                f'Inhabitants: {inhabitants_string}\n'
                f'Species in enclosure: {self.__species_in_enclosure}'
                f'Portions of food: {self._food_level}\n\n')

    @property
    def name(self):
        return self.__name

    @property
    def size(self):
        return self.__size

    @property
    def environment(self):
        return self.__environment

    @property
    def cleanliness(self):
        return self.__cleanliness

    @property
    def inhabitants(self):
        return self.__inhabitants

    @property
    def species_in_enclosure(self):
        return self.__species_in_enclosure

    @property
    def food_level(self):
        return self._food_level

    @cleanliness.setter
    def cleanliness(self, level):
        if not (0 <= level <= 100):
            raise ValueError('cleanliness level must be between 0 and 100')
        self.__cleanliness = level

    def appropriate_species(self, animal):
        if self.species_in_enclosure and animal.species.lower() != self.species_in_enclosure:
            print('An incompatible animal already lives here.')
            return False
        if animal.environment_type != self.environment:
            print(f'The enclosure is the wrong environment type for {animal.name}')
            return False
        allowed_sizes = ENVIRONMENT_SIZE.get(animal.species.lower())
        if self.size not in allowed_sizes:
            print(f'The enclosure is an incompatible size for {animal.name}')
            return False
        return True

    def add_animal(self, animal):
        if self.appropriate_species(animal):
            self.__inhabitants.append(animal)
            if not self.__species_in_enclosure:
                self.__species_in_enclosure = animal.species.lower()
            print(f'You have added {animal.name} to the enclosure {self.__name}')
            return True
        return False

    def remove_animal(self, animal):
        if animal in self.__inhabitants:
            self.__inhabitants.remove(animal)
            print(f'You have removed {animal.name} from the enclosure {self.name}')
            if not self.__inhabitants:
                self.__species_in_enclosure = None
                print(f'Enclosure {self.name} is now empty.')
            return True
        else:
            print(f'{animal} was not found in enclosure {self.name}. No animals have been removed.')
            return False

    def cleaning_required(self):
        if self.cleanliness <= 30:
            print(f'The enclosure {self.name} needs to be cleaned up today!')
            return True
        if self.cleanliness < 50:
            print(f'The enclosure {self.name} needs to be cleaned in the next 3 days.')
            return True
        if self.cleanliness < 80:
            print(f'The enclosure {self.name} needs to be cleaned up within 1 week.')
            return True
        print(f'The enclosure {self.name} does not need cleaning yet.')
        return False

    def clean_enclosure(self):
        self.__cleanliness = 100
        print(f'The enclosure {self.name} has been fully cleaned up.')

    def add_food(self, amount: int):
        if amount <= 0:
            raise ValueError('The amount must be greater than 0')
        self._food_level += amount

    def consume_food(self, amount: int):
        if amount <= 0:
            raise ValueError('The amount must be greater than 0')
        if amount > self._food_level:
            raise ValueError('The amount cannot be greater than the amount of available food.')
        self._food_level -= amount

class OpenAir(Enclosure):
    pass

class Vivarium(Enclosure):
    pass

class Aviary(Enclosure):
    pass

