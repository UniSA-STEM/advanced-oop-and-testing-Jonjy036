"""
File: veterinarian.py
Description: the veterinarian child module (staff) for the advanced OOP and Testing Assignment.
Author: Jozef Jones
ID: 110484756
Username: jonjy036
This is my own work as defined by the University's Academic Integrity Policy.
"""
from staff import Staff
from datetime import date


class Veterinarian(Staff):
    """
        initilise the child class of Staff - veterinarian.

        name = name of staff (full name)
        staff_number = a number created to identify the staff member
        hospital_list = a list to store animals when they are suffering from illness or injury
            not an enclosure to seperate the areas for display from the back of house areas.
        """

    def __init__(self, name, staff_number):
        super().__init__(name, staff_number)
        self._hospital_list = []

    """getters and setters for relevant attributes."""

    @property
    def hospital_list(self):
        return self._hospital_list

    @hospital_list.setter
    def hospital_list(self, hospital_list):
        self._hospital_list = hospital_list

    def perform_health_check(self, animal, zoo_manager):
        """perofrms a health chceck on a dedsignated animal and creates a report if required."""
        print(f'Health check for {animal.name} performed by {self.name} on {date.today()}')

        report_required = input('Does the healthcheck require a report to be raised? (yes/no): ').lower()
        if report_required != 'yes':
            print('Health check complete. No report needed.')
            return

        report_type = input('What type of report do you want to make? (injury/illness/behaviour): ').lower()
        if report_type not in self.ALLOWED_REPORT_TYPES:
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

        """create the report based on inputs"""
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
        self.update_health_status(animal, severity, zoo_manager)

    def update_health_status(self, animal, severity: int, manager):
        """if required update the health status of an instance of animal. called in perform health check"""
        if severity >= 3 and animal.in_good_health:
            self.move_animal_to_hospital(animal, manager)
        elif severity >= 2 and not animal.in_good_health:
            self.move_animal_out_of_hospital(animal, manager)

    def move_animal_to_hospital(self, animal, manager):
        """defines the condition under which an animal is removed from their enclosure and
        sent to hospital."""
        if animal.enclosure and animal in animal.enclosure.inhabitants:
            animal.original_enclosure = animal.enclosure
            manager.remove_animal_from_enclosure(animal, animal.enclosure)
        if animal not in self.hospital_list:
            self.hospital_list.append(animal)
        animal.in_good_health = False

    def move_animal_out_of_hospital(self, animal, manager):
        """When the animal has recovered sufficiently the animal is removed from hospital
        and is placed back in their original enclosure."""
        if animal in self.hospital_list:
            self.hospital_list.remove(animal)
        if hasattr(animal, 'original_enclosure') and animal.original_enclosure is not None:
            manager.assign_animal_to_enclosure(animal, animal.original_enclosure)
        animal.in_good_health = True
