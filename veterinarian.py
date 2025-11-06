'''
File: veterinarian.py
Description: the veterinarian child module (staff) for the advanced OOP and Testing Assignment.
Author: Jozef Jones
ID: 110484756
Username: jonjy036
This is my own work as defined by the University's Academic Integrity Policy.
'''
from staff import Staff
from animal import Animal
from datetime import date

class Veterinarian(Staff):
    def __init__(self, name, staff_number):
        super().__init__(name, staff_number)

    def perform_health_check(self, animal):
        print(f'Health check for {animal.name} performed by {self.name} on {date.today()}')

        report_required = input('Does the healthcheck require a report to be raised? (yes/no): ').lower()
        if report_required != 'yes':
            print('Health check complete. No report needed.')
            return

        report_type = input('What type of report do you want to make? (injury/illness/behaviour): ').lower()
        if report_type != self.ALLOWED_REPORT_TYPES:
            print(f'invalid report type: {report_type}. Report not created.')
            return

        description = input('Please describe the issue: ')
        severity = int(input('What is the severity of the issue? (1-5): '))
        try:
            if not (1 <= severity <= 5):
                raise ValueError()
        except ValueError:
            print('Invalid severity. No report created.')
            return

        treatment_plan = input('please enter a treatment plan (optional): ')
        notes = input('please enter any notes (optional): ')

        self.report(
            animal=animal,
            description=description,
            severity=severity,
            report_type=report_type,
            treatment_plan=treatment_plan,
            notes=notes,
            date_reported=date.today()
        )
        print(f'Report created for {animal.name} on {date.today()}')