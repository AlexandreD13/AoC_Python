import re

from src.IDay import IDay

class Day3_2024(IDay):

    def __init__(self, is_real_data):
        super().__init__()

        self.name = "day3"
        self.year = "2024"

        if is_real_data:
            self.input: str = f"src/inputs/2024/{self.name}.txt"
        else:
            self.input: str = f"src/inputs/2024/{self.name}_test.txt"

        self.data: list[str] = self.import_string_data()

    def __str__(self) -> str:
        return f"['{self.data[0][:20]}...', '{self.data[1][:20]}...'] (...)"

    def part1(self) -> int:
        pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
        total = 0

        for line in self.data:
            matches = pattern.findall(line)

            for x, y in matches:
                total += int(x) * int(y)

        return total

    def part2(self) -> int:
        pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)")
        total = 0
        mul_enabled = True

        for line in self.data:
            instructions = re.finditer(pattern, line)

            for match in instructions:
                if line[match.start():match.end()].startswith("mul") and mul_enabled:
                    x, y = line[match.start():match.end()][4:-1].split(",")
                    total += int(x) * int(y)

                elif line[match.start():match.end()] == "do()":
                    mul_enabled = True

                elif line[match.start():match.end()] == "don't()":
                    mul_enabled = False

        return total

