'''
File: test_enclosure.py
Description: the enclosure testing module for the advanced OOP and Testing Assignment.
Author: Jozef Jones
ID: 110484756
Username: jonjy036
This is my own work as defined by the University's Academic Integrity Policy.
'''
import pytest
from datetime import date
import enclosure
import mammal
import bird
import reptile


class TestEnclosure:

    @pytest.fixture
    def open_air(self):
        return enclosure.OpenAir('openair1','extra large', 'savannah')

    @pytest.fixture
    def aviary(self):
        return enclosure.Aviary('aviary1', 'medium', 'forest', cleanliness=75)

    @pytest.fixture
    def vivarium(self):
        return enclosure.Vivarium('vivarium1', 'medium', 'forest', cleanliness=45)

    @pytest.fixture
    def open_air_aquatic(self):
        return enclosure.OpenAir('openair2', 'large', 'aquatic', cleanliness=25)

    @pytest.fixture
    def aviary_2(self):
        return enclosure.Aviary('aviary_2', 'medium', 'forest', cleanliness=80)

    @pytest.fixture
    def lion(self):
        return mammal.Lion('Simba', date(2020, 3, 21), 'male')

    @pytest.fixture
    def kookaburra(self):
        return bird.Kookaburra('Koko', date(2020, 4,1), 'female')

    @pytest.fixture
    def python(self):
        return reptile.Python('Monty', date(2002, 1, 21), 'male')

    @pytest.fixture
    def crocodile(self):
        return reptile.Crocodile('Bert', date(2020, 5, 5), 'male')

    def test_lion_open_air_appropriate_species(self, open_air, lion, kookaburra):
        assert open_air.appropriate_species(lion) is True
        assert open_air.appropriate_species(kookaburra) is False

    def test_kookaburra_aviary_appropriate_species(self, aviary, kookaburra):
        assert aviary.appropriate_species(kookaburra) is True

    def test_python_vivarium_appropriate_species(self, vivarium, python):
        assert vivarium.appropriate_species(python) is True

    def test_crocodile_open_air_aquatic_appropriate_species(self, open_air_aquatic, crocodile, python, lion):
        assert open_air_aquatic.appropriate_species(crocodile) is True
        assert open_air_aquatic.appropriate_species(python) is False
        assert open_air_aquatic.appropriate_species(lion) is False

    def test_cleaning_required(self, open_air, aviary, vivarium, open_air_aquatic, aviary_2):
        assert open_air.cleaning_required() is False
        assert aviary.cleaning_required() is True
        assert vivarium.cleaning_required() is True
        assert open_air_aquatic.cleaning_required() is True
        assert aviary_2.cleaning_required() is False
