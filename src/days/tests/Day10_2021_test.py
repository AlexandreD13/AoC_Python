from src.days.implementations.Day10_2021 import Day10_2021


class TestDay10:
    day = Day10_2021(False)

    def test_part1(self):
        assert self.day.part1() == 26397

    def test_part2(self):
        assert self.day.part2() == 288957
