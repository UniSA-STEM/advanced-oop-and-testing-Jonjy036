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
    snake_city = Vivarium('Snake City', 'medium', 'forest', 90)
    dragon_lair = Vivarium('Dragon Lair', 'small', 'desert', 60)
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

def staff_assignment(manager: ZooManager, staff, enclosures):
    '''Assign staffs to enclosures.'''
    keeper_1, keeper_2, _ = staff
    lion_enclosure, forest_paddock, croc_creek, snake_city, dragon_lair, birds_nest, penguin_pool = enclosures

    print('\nAssigning Staff to enclosures\n')
    manager.assign_zookeeper_to_enclosure(keeper_1, lion_enclosure)
    manager.assign_zookeeper_to_enclosure(keeper_1, croc_creek)
    manager.assign_zookeeper_to_enclosure(keeper_2, birds_nest)
    manager.assign_zookeeper_to_enclosure(keeper_2, penguin_pool)

def check_cleaning(enclosures):
    '''Check if enclosures need cleaning.'''
    lion_enclosure, forest_paddock, croc_creek, snake_city, dragon_lair, birds_nest, penguin_pool = enclosures

    print('\nChecking for enclosures which need to be cleaned\n')
    for enclosure in enclosures:
        enclosure.cleaning_required()

def feeding_activities(staff, animals, enclosures):
    '''Perform feeding activities'''
    keeper_1, keeper_2, _ = staff
    simba, nala, snappy, monty, drogon, eddi, koko, pingu = animals
    lion_enclosure, forest_paddock, croc_creek, snake_city, dragon_lair, birds_nest, penguin_pool = enclosures

    print('Feeding time!')

    keeper_1.feed_animals(lion_enclosure)
    print(simba.eat(simba.enclosure))
    print(nala.eat(nala.enclosure))
    print(simba.eat(simba.enclosure))
    print(drogon.eat(drogon.enclosure))

def health_checks(vet, animals, zoo_manager):
    '''Perform health checks'''
    simba = animals[0]
    nala = animals[1]

    vet.perform_health_check(simba, zoo_manager)

    print('\nhospital list:')
    if len(vet.hospital_list) > 0:
        for animal in vet.hospital_list:
            print(animal.name)
    else:
        print('\nno animals are in hospital\n')

    vet.perform_health_check(nala, zoo_manager)

    print('\nhospital list:')
    if len(vet.hospital_list) > 0:
        for animal in vet.hospital_list:
            print(animal.name)
    else:
        print('\nno animals are in hospital\n')

def main():

    print('***Creating a manager***')
    manager = create_manager()
    print_zoo_reports(manager)

    print('\n***Creating animals***')
    animals = create_animals()
    simba, nala, snappy, monty, drogon, eddi, koko, pingu = animals
    print_zoo_reports(manager)

    print('\n***Creating enclosures***')
    enclosures = create_enclosures()
    lion_enclosure, forest_paddock, croc_creek, snake_city, dragon_lair, birds_nest, penguin_pool = enclosures
    print_zoo_reports(manager)

    print('\n***Assigning animals to enclosures***')
    enclosure_assignment(manager, animals, enclosures)
    print_zoo_reports(manager)

    print('\n***Creating staff***')
    staff = create_staff()
    keeper_1, keeper_2, vet = staff

    print('\n***assinging keepers to enclosures***')
    staff_assignment(manager, staff, enclosures)

    print('\n***feeding and cleaning enclosures***')
    check_cleaning(enclosures)
    print('\n***Get Kevin (zookeeper1) to clean the lion enclosure.***')
    keeper_1.clean_enclosure(lion_enclosure)
    check_cleaning(enclosures)

    feeding_activities(staff, animals, enclosures)

    print('***health reporting and hospital transfer.***')
    health_checks(vet, animals, manager)





if __name__ == '__main__':
    main()