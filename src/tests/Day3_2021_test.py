from src.implementations.Day3_2021 import Day3_2021


class TestDay3:
    day = Day3_2021(False)

    def test_part1(self):
        assert self.day.part1() == 198

    def test_part2(self):
        assert self.day.part2() == 230
