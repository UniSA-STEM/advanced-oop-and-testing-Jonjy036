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

class TestZookeeper:

    @pytest.fixture
    def zookeeper(self):
        return zookeeper.Zookeeper('John', 1003)

    @pytest.fixture
    def test_animal(self):
        return mammal.Lion('Simba', date(2019, 12, 25), 'male')

    @pytest.fixture
    def test_enclosure(self):
        enc = enclosure.OpenAir('testEnclosure', 'extra large', 'savannah')
        enc._OpenAir__inhabitants = []
        enc._OpenAir__food_level = 0
        enc.cleanliness = 50
        return enc

    def test_clean_enclosure(self, zookeeper, test_enclosure):
        zookeeper.clean_enclosure(test_enclosure)
        assert test_enclosure.cleanliness == 100


    def test_clean_enclosure_invalid(self, zookeeper):
        with pytest.raises(ValueError):
            zookeeper.clean_enclosure(None)

    def test_feed_animals(self, zookeeper, test_enclosure, test_animal):
        test_enclosure.inhabitants.append(test_animal)
        zookeeper.feed_animals(test_enclosure.inhabitants, test_enclosure)
        expected_food_level = len(test_enclosure.inhabitants)
        assert test_enclosure.food_level == expected_food_level

    def test_feed_enclosure_no_inhabitants(self, zookeeper, test_enclosure):
        test_enclosure._OpenAir__inhabitants = []
        test_enclosure._OpenAir__food_level = 0
        zookeeper.feed_animals(test_enclosure.inhabitants, test_enclosure)
        assert test_enclosure.food_level == 0

    def test_feed_enclosure_no_enclosure(self, zookeeper, test_enclosure):
        with pytest.raises(ValueError):
            zookeeper.feed_animals([],None)

