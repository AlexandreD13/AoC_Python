from src.IDay import IDay


class Day11_2021(IDay):

    def __init__(self, is_real_data):
        super().__init__()

        self.name = "day11"
        self.year = "2021"

        if is_real_data:
            self.input: str = f"src/inputs/2021/{self.name}.txt"
        else:
            self.input: str = f"src/inputs/2021/{self.name}_test.txt"

        self.data: dict = self.map_octopuses(self.import_string_data())

        self.steps_p1: int = 100
        self.steps_p2: int = 0

    def __str__(self) -> str:
        subset = {k: v for k, v in self.data.items() if (0, 0) <= k <= (2, 0)}
        return f"{subset} (...)"

    def part1(self) -> int:
        flashes: int = 0
        octopuses = self.data.copy()

        while self.steps_p1 > 0:
            for key, value in octopuses.items():
                if value >= 9:
                    octopuses[key] = 0
                    flashes += 1

                    octopuses[(key[0] - 1, key[1] - 1)] += 1
                    octopuses[(key[0] - 1, key[1])] += 1
                    octopuses[(key[0] - 1, key[1] + 1)] += 1

                    octopuses[(key[0], key[1] - 1)] += 1
                    octopuses[(key[0], key[1] + 1)] += 1

                    octopuses[(key[0] + 1, key[1] - 1)] += 1
                    octopuses[(key[0] + 1, key[1])] += 1
                    octopuses[(key[0] + 1, key[1] + 1)] += 1
                else:
                    octopuses[key] += 1

            self.steps_p1 -= 1

        return flashes

    @staticmethod
    def map_octopuses(data: list[str]) -> dict:
        octopuses: dict = {}

        for y in range(len(data)):
            for x in range(len(data[y])):
                octopuses[(x, y)] = int(data[y][x])

        return octopuses

    def part2(self) -> int:
        return 0
