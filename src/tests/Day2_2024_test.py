from src.implementations.Day2_2024 import Day2_2024


class TestDay2:
    day = Day2_2024(False)

    def test_part1(self):
        assert self.day.part1() == 2

    def test_part2(self):
        assert self.day.part2() == 4
