from src.implementations.Day4_2015 import Day4_2015


class TestDay4:
    day = Day4_2015(False)

    def test_part1(self):
        assert self.day.part1() == 282749

    def test_part2(self):
        assert self.day.part2() == 9962624
