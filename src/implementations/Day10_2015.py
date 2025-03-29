from typing import List

from src.IDay import IDay


class Day10_2015(IDay):
    def __init__(self, is_real_data):
        super().__init__()

        self.name = "day10"
        self.year = "2015"

        if is_real_data:
            self.input: str = f"src/inputs/2015/{self.name}.txt"
        else:
            self.input: str = f"src/inputs/2015/{self.name}_test.txt"

        self.data: List[str] = self.import_string_data()

    def __str__(self) -> str:
        return f"{self.data}"

    def part1(self) -> int:

        """

        import re

        s = "12213111"
        segments = re.findall(r'(\d)(\1*)', s)
        result = ["".join(segment) for segment in segments]

        """

        return 0

    def part2(self) -> int:

        return 0
