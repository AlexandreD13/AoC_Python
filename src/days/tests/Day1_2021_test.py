from src.days.implementations.Day1_2021 import Day1_2021


class TestDay1:
    day = Day1_2021(False)

    def test_part1(self):
        assert self.day.part1() == 7

    def test_part2(self):
        assert self.day.part2() == 5
