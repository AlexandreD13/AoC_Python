from src.implementations.Day9_2015 import Day9_2015


class TestDay9:
    day = Day9_2015(False)

    def test_part1(self):
        assert self.day.part1() == 605

    def test_part2(self):
        assert self.day.part2() == 982
