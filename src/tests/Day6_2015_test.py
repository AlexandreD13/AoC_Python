from src.implementations.Day6_2015 import Day6_2015


class TestDay6:
    day = Day6_2015(False)

    def test_part1(self):
        assert self.day.part1() == 1000000

    def test_part2(self):
        assert self.day.part2() == 2000000
