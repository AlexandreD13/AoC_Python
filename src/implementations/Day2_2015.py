from typing import List

from src.IDay import IDay


class Day2_2015(IDay):
    def __init__(self, is_real_data):
        super().__init__()

        self.name = "day2"
        self.year = "2015"

        if is_real_data:
            self.input: str = f"src/inputs/2015/{self.name}.txt"
        else:
            self.input: str = f"src/inputs/2015/{self.name}_test.txt"

        self.data: List[str] = self.import_string_data()

    def __str__(self) -> str:
        return f"{self.data[:5]} (...)"

    def part1(self) -> int:
        """

        """

        total = 0
        for line in self.data:
            length, width, height = map(int, line.split("x"))
            lw, wh, hl = length * width, width * height, height * length
            total += 2 * (lw + wh + hl) + min(lw, wh, hl)

        return total

    def part2(self) -> int:
        """

        """

        total = 0
        for line in self.data:
            length, width, height = sorted(map(int, line.split("x")))
            total += 2 * (length + width) + (length * width * height)

        return total