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

class TestZooManager:

    @pytest.fixture
    def manager(self):
        return zoo_manager.ZooManager('Simone', 1000)

    @pytest.fixture
    def test_animal(self):
        return mammal.Lion('Simba', date(2019, 12, 25), 'male')

    @pytest.fixture
    def test_enclosure(self):
        enc = enclosure.OpenAir('testEnclosure', 'extra large', 'savannah')
        enc._OpenAir__inhabitants = []
        return enc

    @pytest.fixture
    def keeper(self):
        return zookeeper.Zookeeper('John', 1003)

    def test_zoo_manager_initialization(self, manager):
        assert manager is not None
        assert manager.name == 'Simone'
        assert manager.staff_number == 1000
        assert isinstance(manager.zookeeper_assignments, dict)
        assert len(manager.zookeeper_assignments) == 0

    def test_assign_and_remove_animal(self, manager, test_enclosure, test_animal):
        result = manager.assign_animal_to_enclosure(test_animal, test_enclosure)
        assert result is True
        assert test_animal in test_enclosure.inhabitants
        assert test_animal.enclosure == test_enclosure

        result2 = manager.assign_animal_to_enclosure(test_animal, test_enclosure)
        assert result2 is False
        assert test_enclosure.inhabitants.count(test_animal) == 1

        result3 = manager.remove_animal_from_enclosure(test_animal, test_enclosure)
        assert result3 is True
        assert test_animal not in test_enclosure.inhabitants
        assert test_animal.enclosure is None

    def test_assign_animal_invalid(self, manager, test_enclosure, test_animal):
        with pytest.raises(AttributeError):
            manager.assign_animal_to_enclosure(None, test_enclosure)
        with pytest.raises(AttributeError):
            manager.assign_animal_to_enclosure(test_animal, None)

    def test_remove_animal_empty_enclosure(self, manager, test_animal, test_enclosure):
        test_enclosure._OpenAir__inhabitants = []
        result = manager.remove_animal_from_enclosure(test_animal, test_enclosure)
        assert result is False

    def test_remove_animal_invalid(self, manager, test_enclosure, test_animal):
        with pytest.raises(AttributeError):
            manager.remove_animal_from_enclosure(None, test_enclosure)
        with pytest.raises(AttributeError):
            manager.remove_animal_from_enclosure(test_animal, None)

    def test_assign_zookeeper_to_enclosure(self, manager, keeper, test_enclosure):
        manager.assign_zookeeper_to_enclosure(keeper, test_enclosure)
        assignments = manager.zookeeper_assignments
        assert keeper in assignments
        assert test_enclosure in assignments[keeper]

    def test_assign_zookeeper_duplication(self, manager, keeper, test_enclosure):
        manager.assign_zookeeper_to_enclosure(keeper, test_enclosure)
        manager.assign_zookeeper_to_enclosure(keeper, test_enclosure)
        assignments = manager.zookeeper_assignments
        assert assignments[keeper].count(test_enclosure) == 1

    def test_assign_zookeeper_invalid(self, manager, keeper, test_enclosure):
        with pytest.raises(AttributeError):
            manager.assign_zookeeper_to_enclosure(None, test_enclosure)
        with pytest.raises(AttributeError):
            manager.assign_zookeeper_to_enclosure(keeper, None)

    def test_remove_zookeeper_assignment(self, manager, keeper, test_enclosure):
        manager.assign_zookeeper_to_enclosure(keeper, test_enclosure)
        result = manager.remove_zookeeper_assignment(keeper, test_enclosure)
        assert result is True
        assert keeper not in manager.zookeeper_assignments

    def test_remove_zookeeper_not_assigned(self, manager, keeper, test_enclosure):
        result = manager.remove_zookeeper_assignment(keeper, test_enclosure)
        assert result is False

    def test_remove_zookeeper_invalid(self, manager, keeper, test_enclosure):
        with pytest.raises(AttributeError):
            manager.remove_zookeeper_assignment(None, test_enclosure)
        with pytest.raises(AttributeError):
            manager.remove_zookeeper_assignment(keeper, None)

    def test_get_enclosures_for_zookeeper(self, manager, keeper, test_enclosure):
        manager.assign_zookeeper_to_enclosure(keeper, test_enclosure)
        enclosures = manager.get_enclosures_for_zookeeper(keeper)
        assert enclosures == [test_enclosure]

    def test_get_enclosures_for_zookeeper_no_assignments(self, manager, keeper):
        enclosures = manager.get_enclosures_for_zookeeper(keeper)
        assert enclosures == []

    def test_move_animal_to_hospital_and_remove(self, manager, test_animal, test_enclosure):
        manager.assign_animal_to_enclosure(test_animal, test_enclosure)
        assert test_animal in test_enclosure.inhabitants
        assert test_animal.enclosure == test_enclosure

        manager.move_animal_to_hospital(test_animal)
        assert test_animal not in test_enclosure.inhabitants
        assert test_animal in manager.hospital_list
        assert test_animal.in_good_health is False
        assert test_animal.original_enclosure == test_enclosure

        manager.move_animal_out_of_hospital(test_animal)
        assert test_animal not in manager.hospital_list
        assert test_animal in test_enclosure.inhabitants
        assert test_animal.in_good_health is True