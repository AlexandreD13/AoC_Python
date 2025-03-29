from typing import List, Tuple

from src.IDay import IDay


class Day3_2015(IDay):
    def __init__(self, is_real_data):
        super().__init__()

        self.name = "day3"
        self.year = "2015"

        if is_real_data:
            self.input: str = f"src/inputs/2015/{self.name}.txt"
        else:
            self.input: str = f"src/inputs/2015/{self.name}_test.txt"

        self.data: str = self.import_string_data()[0]

    def __str__(self) -> str:
        return f"{self.data[:50]} (...)"

    def part1(self) -> int:
        """

        """

        x, y = 0, 0
        houses = {(x, y)}

        for character in self.data:
            match character:
                case ">": x += 1
                case "<": x -= 1
                case "^": y += 1
                case "v": y -= 1

            houses.add((x, y))

        return len(houses)

    def part2(self) -> int:
        """

        """

        x1, y1, x2, y2 = 0, 0, 0, 0
        houses1 = {(x1, y1)}
        houses2 = {(x2, y2)}

        for index in range(len(self.data)):
            if index % 2 == 0:
                houses1, x1, y1 = self.addLocation(houses1, index, x1, y1)
            else:
                houses2, x2, y2 = self.addLocation(houses2, index, x2, y2)

        return len(houses1.union(houses2))

    def addLocation(self, houses, index, x, y) -> Tuple[set, int, int]:
        """

        """

        match self.data[index]:
            case ">": x += 1
            case "<": x -= 1
            case "^": y += 1
            case "v": y -= 1

        houses.add((x, y))

        return houses, x, y