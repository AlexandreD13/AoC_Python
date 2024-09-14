from src.days.implementations.Day4_2021 import Day4_2021


class TestDay4:
    day = Day4_2021(False)

    def test_part1(self):
        assert self.day.part1() == 4512

    def test_part2(self):
        assert self.day.part2() == 1924
