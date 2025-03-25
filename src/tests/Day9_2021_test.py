from src.implementations.Day9_2021 import Day9_2021


class TestDay9:
    day = Day9_2021(False)

    def test_part1(self):
        assert self.day.part1() == 15

    def test_part2(self):
        assert self.day.part2() == 1134
