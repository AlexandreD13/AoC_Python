import os
from typing import Any, List

from src.IDay import IDay


class SchoolOfFish:
    def __init__(self, initial_state: List[int]):
        self.group: dict = {
            "0": 0,
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0,
            "7": 0,
            "8": 0,
            "9": 0,
        }

        for i in range(len(initial_state)):
            if initial_state[i] in self.group:
                self.group[initial_state[i]] += 1
            else:
                self.group[initial_state[i]] = 1

        self.days_passed: int = 0

    def state(self) -> int:
        return sum(self.group.values())

    def update(self) -> None:
        for key in self.group:
            if int(key) == 0:
                self.group["7"] += self.group[key]
                self.group["9"] += self.group[key]
                self.group["0"] = 0
            else:
                self.group[str(int(key) - 1)] += self.group[key]
                self.group[key] = 0

        self.days_passed += 1


class Day6_2021(IDay):
    def __init__(self, is_real_data):
        super().__init__()

        self.name = "day6"
        self.year = "2021"

        if is_real_data:
            self.input: str = f"src/inputs/2021/{self.name}.txt"
        else:
            self.input: str = f"src/inputs/2021/{self.name}_test.txt"

        self.data: List[int] = self.custom_import()

        self.CYCLES_P1: int = 80
        self.CYCLES_P2: int = 256

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
        school: SchoolOfFish = SchoolOfFish(self.data)

        for i in range(0, self.CYCLES_P1):
            school.update()

        return school.state()

    def part2(self) -> int:
        school: SchoolOfFish = SchoolOfFish(self.data)

        for i in range(0, self.CYCLES_P2):
            school.update()

        return school.state()
