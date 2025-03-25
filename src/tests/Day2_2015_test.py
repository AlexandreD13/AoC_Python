from src.implementations.Day2_2015 import Day2_2015


class TestDay2:
    day = Day2_2015(False)

    def test_part1(self):
        assert self.day.part1() == 58

    def test_part2(self):
        assert self.day.part2() == 34
