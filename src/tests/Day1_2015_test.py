from src.implementations.Day1_2015 import Day1_2015


class TestDay1:
    day = Day1_2015(False)

    def test_part1(self):
        assert self.day.part1() == -1

    def test_part2(self):
        assert self.day.part2() == 5
