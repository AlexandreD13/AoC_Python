from src.days.implementations.Day5_2021 import Day5_2021


class TestDay5:
    day = Day5_2021(False)

    def test_part1(self):
        assert self.day.part1() == 5

    def test_part2(self):
        assert self.day.part2() == 12
