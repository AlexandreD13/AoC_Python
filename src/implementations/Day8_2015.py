from typing import List

from src.IDay import IDay


class Day8_2015(IDay):
    def __init__(self, is_real_data):
        super().__init__()

        self.name = "day8"
        self.year = "2015"

        if is_real_data:
            self.input: str = f"src/inputs/2015/{self.name}.txt"
        else:
            self.input: str = f"src/inputs/2015/{self.name}_test.txt"

        self.data: List[str] = self.import_string_data()

    def __str__(self) -> str:
        return f"{self.data[:5]} (...)"

    def part1(self) -> int:

        total = 0
        for line in self.data:
            original_length = len(line)
            memory_length = len(eval(line))
            total += original_length - memory_length

        return total

    def part2(self) -> int:

        total = 0
        for line in self.data:
            original_length = len(line)
            encoded_length = 2 + line.count('\\') + line.count('"') + original_length
            total += encoded_length - original_length

        return total
