'''
File: enclosure.py
Description: the enclosure module for the advanced OOP and Testing Assignment.
Author: Jozef Jones
ID: 110484756
Username: jonjy036
This is my own work as defined by the University's Academic Integrity Policy.
'''
class Enclosure:
    def __init__(self, name: str, size, environment, cleanliness=100):
        self.__name = name
        self.__size = size
        self.__environment = environment
        self.__cleanliness = cleanliness
        self.__inhabitants = []
        self.__species_in_enclosure = None

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

    @cleanliness.setter
    def cleanliness(self, level):
        if not (0 <= level <= 100):
            raise ValueError('cleanliness level must be between 0 and 100')
        self.__cleanliness = level

