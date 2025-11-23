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


