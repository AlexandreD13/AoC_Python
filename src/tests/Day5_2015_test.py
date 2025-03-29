from src.implementations.Day5_2015 import Day5_2015


class TestDay5:
    day = Day5_2015(False)

    def test_part1(self):
        assert self.day.part1() == 2

    def test_part2(self):
        assert self.day.part2() == 2
