from typing import List

from src.IDay import IDay


class Day7_2015(IDay):
    def __init__(self, is_real_data):
        super().__init__()

        self.name = "day7"
        self.year = "2015"

        if is_real_data:
            self.input: str = f"src/inputs/2015/{self.name}.txt"
        else:
            self.input: str = f"src/inputs/2015/{self.name}_test.txt"

        self.data: List[str] = self.import_string_data()

        self.instructions = {}
        self.values = {}

        for line in self.data:
            parts = line.split(" -> ")
            self.instructions[parts[1]] = parts[0].split()

    def __str__(self) -> str:
        return f"{self.data[:5]} (...)"

    def part1(self) -> int:
        self.values = {}
        return self.evaluate("a")

    def part2(self) -> int:
        self.values = {"b": self.part1()}
        return self.evaluate("a")

    def evaluate(self, wire):
        if wire in self.values:
            return self.values[wire]

        if wire.isdigit():
            return int(wire)

        expr = self.instructions[wire]

        if len(expr) == 1:
            result = self.evaluate(expr[0])
        elif "AND" in expr:
            result = self.evaluate(expr[0]) & self.evaluate(expr[2])
        elif "OR" in expr:
            result = self.evaluate(expr[0]) | self.evaluate(expr[2])
        elif "LSHIFT" in expr:
            result = self.evaluate(expr[0]) << int(expr[2])
        elif "RSHIFT" in expr:
            result = self.evaluate(expr[0]) >> int(expr[2])
        elif "NOT" in expr:
            result = ~self.evaluate(expr[1]) & 0xFFFF
        else:
            raise ValueError(f"Unknown instruction: {expr}")

        self.values[wire] = result
        return result
