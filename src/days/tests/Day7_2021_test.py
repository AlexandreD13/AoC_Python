from src.days.implementations.Day7_2021 import Day7_2021


class TestDay7:
    day = Day7_2021(False)

    def test_part1(self):
        assert self.day.part1() == 37

    def test_part2(self):
        assert self.day.part2() == 168
