'''
File: enclosure.py
Description: the enclosure module for the advanced OOP and Testing Assignment.
Author: Jozef Jones
ID: 110484756
Username: jonjy036
This is my own work as defined by the University's Academic Integrity Policy.
'''
from species_data import ENVIRONMENT_SIZE, REPTILE_OPENAIR_SPECIES, REPTILE_VIVARIUM_SPECIES
from mammal import Mammal
from reptile import Reptile
from bird import Bird



class Enclosure:
    ALLOWED_SIZES = ['extra small', 'small', 'medium', 'large', 'extra large']
    enclosure_list = []

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

        Enclosure.enclosure_list.append(self)

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

    @cleanliness.setter
    def cleanliness(self, level):
        if not (0 <= level <= 100):
            raise ValueError('cleanliness level must be between 0 and 100')
        self.__cleanliness = level

    @property
    def inhabitants(self):
        return self.__inhabitants

    @property
    def species_in_enclosure(self):
        return self.__species_in_enclosure

    @species_in_enclosure.setter
    def species_in_enclosure(self, species):
        self.__species_in_enclosure = species

    @property
    def food_level(self):
        return self._food_level

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

        elif isinstance(animal, Mammal):
            if not isinstance(self, OpenAir):
                print(f'Mammals such as {animal.name} must be housed in Open Air enclosures!')
                return False

        elif isinstance(animal, Bird):
            if not isinstance(self, Aviary):
                print(f'Birds such as {animal.name} must be housed in Aviary enclosures!')
                return False

        elif isinstance(animal, Reptile):
            if isinstance(self, Vivarium):
                if animal.species.lower() not in REPTILE_VIVARIUM_SPECIES:
                    print(f'Animals such as {animal.species}s cannot be housed in a vivarium!')
                    return False

            elif isinstance(self, OpenAir):
                if animal.species.lower() not in REPTILE_OPENAIR_SPECIES:
                    print(f'Animals such as {animal.species}s cannot be housed in an open air enclosures!')
                    return False

            else:
                print(f'Reptiles must be housed in either Open Air enclosures or Vivariums, depending on species.')

        return True

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

class OpenAir(Enclosure):
    pass

class Vivarium(Enclosure):
    pass

class Aviary(Enclosure):
    pass

