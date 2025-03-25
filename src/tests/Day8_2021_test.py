from src.implementations.Day8_2021 import Day8_2021


class TestDay8:
    day = Day8_2021(False)

    def test_part1(self):
        assert self.day.part1() == 26

    def test_part2(self):
        assert self.day.part2() == 61229
