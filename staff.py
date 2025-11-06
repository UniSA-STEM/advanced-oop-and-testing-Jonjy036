'''
File: staff.py
Description: the staff module for the advanced OOP and Testing Assignment.
Author: Jozef Jones
ID: 110484756
Username: jonjy036
This is my own work as defined by the University's Academic Integrity Policy.
'''
from reports import Report

class Staff:
    ALLOWED_REPORT_TYPES = ['injury', 'illness', 'behaviour']

    def __init__(self, name: str, staff_number: int):
        self.__name = name
        self.__staff_number = staff_number
        self.__reports = {}

    def __str__(self):
        return (f'Name: {self.__name}\n'
                f'Staff number: {self.__staff_number}\n')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def staff_number(self):
        return self.__staff_number

    def report(self, animal, report_type, description, date_reported, severity,
               treatment_plan='', notes=''):
        report_type_lower = report_type.lower()
        if report_type_lower not in self.ALLOWED_REPORT_TYPES:
            raise ValueError(f'Report type must be one of {self.ALLOWED_REPORT_TYPES}')

        report = Report(
            animal=animal,
            report_type=report_type_lower,
            description=description,
            date_reported=date_reported,
            severity=severity,
            treatment_plan=treatment_plan,
            notes=notes
        )

        if animal not in self.__reports:
            self.__reports[animal] = []
        self.__reports[animal].append(report)

        print(f'{report_type_lower} report added for {animal.name} by {self.name}.')

    def get_all_reports(self):
        all_reports = []
        for reports in self.__reports.values():
            all_reports.extend(reports)
        return all_reports

    def get_animal_reports(self, animal):
        return self.__reports.get(animal, [])