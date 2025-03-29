import pytest

from src.implementations.Day7_2015 import Day7_2015


class TestDay7:
    day = Day7_2015(False)

    def test_part1(self):
        with pytest.raises(KeyError):
            self.day.part1()

    def test_part2(self):
        with pytest.raises(KeyError):
            self.day.part2()
