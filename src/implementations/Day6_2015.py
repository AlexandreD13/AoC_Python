from typing import List, Tuple, Any

from src.IDay import IDay


class Day6_2015(IDay):
    def __init__(self, is_real_data):
        super().__init__()

        self.name = "day6"
        self.year = "2015"

        if is_real_data:
            self.input: str = f"src/inputs/2015/{self.name}.txt"
        else:
            self.input: str = f"src/inputs/2015/{self.name}_test.txt"

        self.data: List[str] = self.import_string_data()

        self.grid = {}

    def __str__(self) -> str:
        return f"{self.data[:5]} (...)"

    def part1(self) -> int:
        self.grid = {}
        for line in self.data:
            command, start, end = self.parse_command(line)
            self.apply_command_part1(command, start, end)

        return sum(self.grid.values())

    def part2(self) -> int:
        self.grid = {}
        for line in self.data:
            command, start, end = self.parse_command(line)
            self.apply_command_part2(command, start, end)

        return sum(self.grid.values())

    @staticmethod
    def parse_command(line) -> Tuple[Any, List[int], List[int]]:
        line = line.split(" ")

        if len(line) == 4:
            command = line[0]
            start = tuple(map(int, line[1].split(",")))
            end = tuple(map(int, line[3].split(",")))

        if len(line) == 5:
            command = line[0] + " " + line[1]
            start = tuple(map(int, line[2].split(",")))
            end = tuple(map(int, line[4].split(",")))

        return command, start, end

    def apply_command_part1(self, command, start, end) -> None:
        for i in range(int(start[0]), int(end[0]) + 1):
            for j in range(int(start[1]), int(end[1]) + 1):
                if (i, j) not in self.grid:
                    self.grid[(i, j)] = 0

                if command == "turn off":
                    self.grid[(i, j)] = 0
                if command == "turn on":
                    self.grid[(i, j)] = 1
                if command == "toggle":
                    self.grid[(i, j)] = 1 - self.grid[(i, j)]

    def apply_command_part2(self, command, start, end) -> None:
        for i in range(int(start[0]), int(end[0]) + 1):
            for j in range(int(start[1]), int(end[1]) + 1):
                if (i, j) not in self.grid:
                    self.grid[(i, j)] = 0

                if command == "turn off":
                    if self.grid[(i, j)] > 0:
                        self.grid[(i, j)] -= 1
                if command == "turn on":
                    self.grid[(i, j)] += 1
                if command == "toggle":
                    self.grid[(i, j)] += 2