from src.days.implementations.Day6_2021 import Day6_2021


class TestDay6:
    day = Day6_2021(False)

    def test_part1(self):
        assert self.day.part1() == 5934

    def test_part2(self):
        assert self.day.part2() == 26984457539
