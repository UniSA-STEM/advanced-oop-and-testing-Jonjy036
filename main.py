'''
File: main.py
Description: the main module for the advanced OOP and Testing Assignment.
Author: Jozef Jones
ID: 110484756
Username: jonjy036
This is my own work as defined by the University's Academic Integrity Policy.
'''
from datetime import date

from animal import Animal
from mammal import Lion, Chimpanzee, Dingo
from reptile import Python, BeardedDragon, Crocodile
from bird import Eagle, Kookaburra, Penguin

from enclosure import OpenAir, Vivarium, Aviary

from staff import Staff
from zookeeper import Zookeeper
from zoo_manager import ZooManager
from veterinarian import Veterinarian

from reports import Report


def create_manager():
    manager = ZooManager('Simone', 1001)
    return manager

def create_animals():
    '''Create a number of animals to be used in the demonstration of the system.'''
    simba = Lion('Simba', date(2018, 5, 12),'male')
    nala = Lion('Nala', date(2018, 6, 2),'female', True)
    snappy = Crocodile('Snappy', date(2018, 5, 12), 'male')
    monty = Python('Monty', date(2018, 5, 12), 'male')
    drogon = BeardedDragon('Drogon', date(2018, 5, 12), 'male')
    eddi = Eagle('Eddi', date(2018, 5, 12), 'female', True)
    koko = Kookaburra('Koko', date(2018, 5, 12), 'female')
    pingu = Penguin('Pingu', date(2018, 5, 12), 'male')
    return simba, nala, snappy, monty, drogon, eddi, koko, pingu

def create_staff():
    '''Create a number of staff to be used in the demonstration of the system.'''
    keeper_1 = Zookeeper('Kevin', 1002)
    keeper_2 = Zookeeper('Karen', 1003)
    vet = Veterinarian('Vicky', 1004)
    return keeper_1, keeper_2, vet

def create_enclosures():
    '''Create a number of enclosures to be used in the demonstration of the system.'''
    lion_enclosure = OpenAir('Lion Enclosure', 'extra large', 'savannah', 45)
    forest_paddock = OpenAir('Forest Paddock', 'large', 'forest', 80)
    croc_creek = OpenAir('Croc Creek', 'large', 'aquatic', 25)
    snake_city = Vivarium('snake_city', 'medium', 'forest', 90)
    dragon_lair = Vivarium('dragon_lair', 'small', 'desert', 60)
    birds_nest = Aviary('Birds Nest', 'large', 'savannah', 70)
    penguin_pool = Aviary('Penguin Pool', 'large', 'aquatic', 55)
    return lion_enclosure, forest_paddock, croc_creek, snake_city, dragon_lair, birds_nest, penguin_pool

def print_zoo_reports(manager: ZooManager):
    '''Print reports for animals and enclosures.'''
    manager.animal_report()
    manager.enclosure_report()

def enclosure_assignment(manager: ZooManager, animals, enclosures):
    '''Assign enclosures to animals.'''
    simba, nala, snappy, monty, drogon, eddi, koko, pingu = animals
    lion_enclosure, forest_paddock, croc_creek, snake_city, dragon_lair, birds_nest, penguin_pool = enclosures

    print('\nAssigning Animals to enclosures\n')
    for animal, enclosure in [
        (simba, lion_enclosure),
        (nala, lion_enclosure),
        (snappy, croc_creek),
        (monty, snake_city),
        (drogon, dragon_lair),
        (eddi, birds_nest),
        (koko, birds_nest),
        (pingu, penguin_pool),
    ]:
        manager.assign_animal_to_enclosure(animal, enclosure)

def main():

    manager = create_manager()
    animals = create_animals()
    enclosures = create_enclosures()

    enclosure_assignment(manager, animals, enclosures)

if __name__ == '__main__':
    main()