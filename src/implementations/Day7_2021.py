import os
from typing import Any

from src.IDay import IDay


class Day7_2021(IDay):

    def __init__(self, is_real_data):
        super().__init__()

        self.name = "day7"
        self.year = "2021"

        if is_real_data:
            self.input: str = f"src/inputs/2021/{self.name}.txt"
        else:
            self.input: str = f"src/inputs/2021/{self.name}_test.txt"

        self.data: list[int] = self.custom_import()

    def __str__(self) -> str:
        return f"{self.data[:5]} (...)"

    def custom_import(self) -> Any:
        if os.path.exists(self.input):
            with open(self.input, "r") as file:
                line = file.read().split(",")
                return [int(x) for x in line]
        else:
            raise FileExistsError(f"File '{self.input}' does not exist.")

    def part1(self) -> int:
        median = sorted(self.data)[len(self.data) // 2]
        return sum([abs(median - i) for i in self.data])

    def part2(self) -> int:
        mean = sum(self.data) // len(self.data) + 1
        return sum([abs(mean - i) * (abs(mean - i) + 1) // 2 for i in self.data])
