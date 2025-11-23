import pytest
from datetime import date
import animal
import mammal

class TestMammal:

    @pytest.fixture
    def male_lion(self):
        return mammal.Lion("Simba", date(2020, 3, 21), "male")

    @pytest.fixture
    def female_lion(self):
        return mammal.Lion("Nala", date(2021, 11, 30), "female", True)

    @pytest.fixture
    def male_chimpanzee(self):
        return mammal.Chimpanzee("Bubbles", date(2011, 5, 5), "male")

    @pytest.fixture
    def female_chimpanzee(self):
        return mammal.Chimpanzee("Squeeks", date(2012, 10, 15), "female", False)

    @pytest.fixture
    def male_dingo(self):
        return mammal.Dingo("Bruce", date(2023, 3, 9), "male")

    @pytest.fixture
    def female_dingo(self):
        return mammal.Dingo("Sheila", date(2018, 1, 22), "female", True)

    def test_mammal_initialization(self, male_lion, female_lion, male_chimpanzee, female_chimpanzee, male_dingo, female_dingo):
        assert male_lion.name == "Simba"
        assert female_lion.name == "Nala"
        assert male_chimpanzee.name == "Bubbles"
        assert female_chimpanzee.name == "Squeeks"
        assert male_dingo.name == "Bruce"
        assert female_dingo.name == "Sheila"

    def test_mammal_make_sound(self, male_lion, female_chimpanzee, female_dingo):
        assert male_lion.make_sound() == 'ROOOAAAARRRRR!!!!'
        assert female_chimpanzee.make_sound() == 'OOOHHH OOOHH AAHHHHHH AHHHHHHHH'
        assert female_dingo.make_sound() == 'OOOOOOOHHHHHHHHHHOOOOO'

    def test_mammal_nurse_young(self, female_lion, female_chimpanzee, female_dingo, male_lion):
        assert female_lion.nurse_young() == 'Nala is nursing young.'
        assert female_dingo.nurse_young() == 'Sheila is nursing young.'

        with pytest.raises(PermissionError):
            female_chimpanzee.nurse_young()
        with pytest.raises(PermissionError):
            male_lion.nurse_young()
