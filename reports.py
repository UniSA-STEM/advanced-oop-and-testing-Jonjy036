"""
File: reports.py
Description: the reports module for the advanced OOP and Testing Assignment.
Author: Jozef Jones
ID: 110484756
Username: jonjy036
This is my own work as defined by the University's Academic Integrity Policy.
"""
from datetime import date

class Report:
    ALLOWED_REPORT_TYPES = ['injury', 'illness', 'behaviour']

    def __init__(self, animal, report_type, description:str, date_reported:date, severity: int, treatment_plan: str, notes: str):
        from animal import Animal
        if not isinstance(animal, Animal):
            raise TypeError(f'The animal must be an instance of Animal or a subclass of Animal')

        report_type_lower = report_type.lower()
        if report_type_lower not in self.ALLOWED_REPORT_TYPES:
            raise ValueError(f'The report type must be one of {self.ALLOWED_REPORT_TYPES}')

        if not (1 <= severity <= 5):
            raise ValueError('The severity must be between 1 and 5')

        self.__animal = animal
        self.__report_type = report_type_lower
        self.__description = description
        self.__date_reported = date_reported
        self.__severity = severity
        self.__treatment_plan = treatment_plan
        self.__notes = notes

    @property
    def animal(self):
        return self.__animal

    @property
    def report_type(self):
        return self.__report_type

    @property
    def description(self):
        return self.__description

    @property
    def date_reported(self):
        return self.__date_reported

    @property
    def severity(self):
        return self.__severity

    @property
    def treatment_plan(self):
        return self.__treatment_plan

    @property
    def notes(self):
        return self.__notes

    def __str__(self):
        return (f'Report:\n'
                f'Date: {self.date_reported}\n'
                f'Animal concerned: {self.animal.name}\n'
                f'Report type: {self.__report_type}\n'
                f'Description: {self.__description}\n'
                f'Severity: {self.__severity}\n'
                f'Treatment plan: {self.__treatment_plan}\n'
                f'Notes: {self.__notes}\n')
