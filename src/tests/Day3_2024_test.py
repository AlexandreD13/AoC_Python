from src.implementations.Day3_2024 import Day3_2024


class TestDay3:
    day = Day3_2024(False)

    def test_part1(self):
        assert self.day.part1() == 161

    def test_part2(self):
        assert self.day.part2() == 48
