from typing import List

from src.IDay import IDay


class Day9_2021(IDay):
    def __init__(self, is_real_data):
        super().__init__()

        self.name = "day9"
        self.year = "2021"

        if is_real_data:
            self.input: str = f"src/inputs/2021/{self.name}.txt"
        else:
            self.input: str = f"src/inputs/2021/{self.name}_test.txt"

        self.data: List[str] = self.import_string_data()

    def __str__(self) -> str:
        return f"{self.data[:1]} (...)"

    def part1(self) -> int:
        return self.calculate_risk_level()

    def part2(self) -> int:
        matrice: List[list[int]] = [*map(list, self.data)]
        basins: List[int] = []

        for i in range(len(matrice)):
            for j in range(len(matrice[i])):
                basins.append(self.get_basin(matrice, i, j))

        basins = sorted(basins, reverse=True)
        return basins[0] * basins[1] * basins[2]

    def calculate_heightmap(self) -> dict:
        height_map: dict = {}

        for y, row in enumerate(self.data):
            for x, height in enumerate(row):
                height_map[(x, y)] = int(height)

        return height_map

    def calculate_risk_level(self) -> int:
        total: int = 0
        low_points: List[(int, int)] = []
        height_map: dict = self.calculate_heightmap()

        for coords, height in height_map.items():
            x, y = coords
            neighbours: tuple = ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
            lowest: bool = True

            for neighbour in neighbours:
                if height_map.get(neighbour, 10) <= height:
                    lowest = False
                    break

            if lowest:
                low_points.append(coords)
                total += height + 1

        return total

    def get_basin(self, matrice: List[List[int]], i: int, j: int) -> int:
        if 0 <= i < len(matrice) and 0 <= j < len(matrice[i]) and matrice[i][j] != "9":
            matrice[i][j] = "9"
            return (
                1
                + self.get_basin(matrice, i - 1, j)
                + self.get_basin(matrice, i + 1, j)
                + self.get_basin(matrice, i, j - 1)
                + self.get_basin(matrice, i, j + 1)
            )

        return 0
