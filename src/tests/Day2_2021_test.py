from src.implementations.Day2_2021 import Day2_2021


class TestDay2:
    day = Day2_2021(False)

    def test_part1(self):
        assert self.day.part1() == 150

    def test_part2(self):
        assert self.day.part2() == 900
