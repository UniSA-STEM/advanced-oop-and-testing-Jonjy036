'''
File: staff.py
Description: the staff module for the advanced OOP and Testing Assignment.
Author: Jozef Jones
ID: 110484756
Username: jonjy036
This is my own work as defined by the University's Academic Integrity Policy.
'''
class Staff:
    def __init__(self, name: str, staff_number: int):
        self.__name = name
        self.__staff_number = staff_number

    def __str__(self):
        return (f'Name: {self.__name}\n'
                f'Staff number: {self.__staff_number}\n')

    @property
    def name(self)
        return self.__name

    @property
    def staff_number(self)
        return self.__staff_number

    @name.setter
    def name(self, name):
        self.__name = name


