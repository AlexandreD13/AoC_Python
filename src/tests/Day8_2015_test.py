from src.implementations.Day8_2015 import Day8_2015


class TestDay8:
    day = Day8_2015(False)

    def test_part1(self):
        assert self.day.part1() == 12

    def test_part2(self):
        assert self.day.part2() == 19
