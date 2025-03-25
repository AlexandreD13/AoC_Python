import os

from collections import Counter
from typing import Any

from src.IDay import IDay


class Day1_2024(IDay):

    def __init__(self, is_real_data):
        super().__init__()

        self.name = "day1"
        self.year = "2024"

        if is_real_data:
            self.input: str = f"src/inputs/2024/{self.name}.txt"
        else:
            self.input: str = f"src/inputs/2024/{self.name}_test.txt"

        self.data: tuple[list[int]] = self.custom_import()

        self.data[0].sort()
        self.data[1].sort()

        self.counter = Counter(self.data[1])

    def __str__(self) -> str:
        return f"({self.data[0][:5]} (...), {self.data[1][:5]} (...))"

    def custom_import(self) -> Any:
        if os.path.exists(self.input):
            with open(self.input, "r") as file:
                left = []
                right = []

                for line in file:
                    tmp = line.strip("\n").split(" ")
                    left.append(int(tmp[0]))
                    right.append(int(tmp[-1]))

                return left, right
        else:
            raise FileExistsError(f"File '{self.input}' does not exist.")

    def part1(self) -> int:
        return sum([abs(self.data[0][x] - self.data[1][x]) for x in range(len(self.data[0]))])

    def part2(self) -> int:
        return sum(self.data[0][x] * self.counter[self.data[0][x]] for x in range(len(self.data[0])))
