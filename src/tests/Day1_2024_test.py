from src.implementations.Day1_2024 import Day1_2024


class TestDay1:
    day = Day1_2024(False)

    def test_part1(self):
        assert self.day.part1() == 11

    def test_part2(self):
        assert self.day.part2() == 31
