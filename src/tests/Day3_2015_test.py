from src.implementations.Day3_2015 import Day3_2015


class TestDay3:
    day = Day3_2015(False)

    def test_part1(self):
        assert self.day.part1() == 2

    def test_part2(self):
        assert self.day.part2() == 11
