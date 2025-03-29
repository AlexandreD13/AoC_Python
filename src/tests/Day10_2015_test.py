from src.implementations.Day10_2015 import Day10_2015


class TestDay10:
    day = Day10_2015(False)

    def test_part1(self):
        assert self.day.part1() == 0

    def test_part2(self):
        assert self.day.part2() == 0
