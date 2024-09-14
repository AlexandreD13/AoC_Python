from src.days.implementations.Day11_2021 import Day11_2021


class TestDay11:
    day = Day11_2021(False)

    def test_part1(self):
        assert self.day.part1() == 1656

    def test_part2(self):
        assert self.day.part2() == 0
