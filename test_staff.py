import pytest
from datetime import date

import staff
import veterinarian
import zookeeper
import zoo_manager
import mammal
import enclosure

class TestStaff:

    @pytest.fixture
    def staff_member(self):
        return staff.Staff('Alice', 1001)

    @pytest.fixture
    def test_animal(self):
        return mammal.Lion('Simba', date(2019, 12,25), 'male')

    def test_staff_initialization(self, staff_member):
        assert staff_member is not None
        assert staff_member.name == 'Alice'
        assert staff_member.staff_number == 1001

    def test_report_type_validation(self, staff_member, test_animal):
        staff_member.report(test_animal, 'injury', 'description', date.today(), 3)
        all_reports = staff_member.get_all_reports()
        assert len(all_reports) == 1
        assert all_reports[0].report_type == 'injury'
        with pytest.raises(ValueError):
            staff_member.report(test_animal, 'invlaid', 'description', date.today(), 3)

class TestVeterinan:

    @pytest.fixture
    def vet(self):
        return veterinarian.Veterinarian('Dr Chris Brown', 1002)

    @pytest.fixture
    def test_animal(self):
        return mammal.Lion('Simba', date(2019, 12, 25), 'male')

    def test_veterinarian_initializasion(self, vet):
        assert vet is not None
        assert vet.name == 'Dr Chris Brown'
        assert vet.staff_number == 1002

    def test_perform_health_check(self, vet, test_animal, monkeypatch):
        inputs = iter(['yes', 'injury', 'health issue', '3', '', ''])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        vet.perform_health_check(test_animal)
        reports = vet.get_all_reports()
        assert len(reports) == 1
        report = reports[0]
        assert report.report_type == 'injury'
        assert report.description == 'health issue'
        assert report.severity == 3

    def test_perform_health_check_no_report(self, vet, test_animal, monkeypatch):
        inputs = iter(['no'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        vet.perform_health_check(test_animal)
        reports = vet.get_all_reports()
        assert len(reports) == 0
