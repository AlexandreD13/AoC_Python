from typing import List

from src.IDay import IDay


class Day3_2021(IDay):
    def __init__(self, is_real_data):
        super().__init__()

        self.name = "day3"
        self.year = "2021"

        if is_real_data:
            self.input: str = f"src/inputs/2021/{self.name}.txt"
        else:
            self.input: str = f"src/inputs/2021/{self.name}_test.txt"

        self.data: List[str] = self.import_string_data()

    def __str__(self) -> str:
        return f"{self.data[:3]} (...)"

    def part1(self) -> int:
        gamma: str = ""
        epsilon: str = ""

        for value in self.find_bit_density(self.data):
            if value > len(self.data) / 2:
                gamma += "1"
                epsilon += "0"
            else:
                gamma += "0"
                epsilon += "1"

        return int(gamma, 2) * int(epsilon, 2)

    def part2(self) -> int:
        oxygen: str = self.find_rating("oxygen")
        co2: str = self.find_rating("co2")

        return int(oxygen, 2) * int(co2, 2)

    def find_rating(self, gas: str) -> str:
        array: list[str] = self.data.copy()
        bit_density: list[int] = self.find_bit_density(array)
        bit_position: int = 0

        while len(array) > 1:
            if gas == "oxygen":
                bit = "1" if bit_density[bit_position] >= len(array) / 2.0 else "0"
            else:
                bit = "0" if bit_density[bit_position] >= len(array) / 2.0 else "1"

            for i in self.find_positions_to_remove(array, bit, bit_position):
                array.pop(i)

            bit_density = self.find_bit_density(array)
            bit_position += 1

        return array[0]

    @staticmethod
    def find_bit_density(data) -> List[int]:
        bit_density: List[int] = [0] * len(data[0])

        for line in data:
            for i, char in enumerate(line):
                bit_density[i] += int(char)

        return bit_density

    @staticmethod
    def find_positions_to_remove(array: List[str], bit: str, bit_position: int) -> List[int]:
        to_remove: list[int] = []

        for i, line in enumerate(array):
            if line[bit_position] != bit:
                to_remove.append(i)

        to_remove.sort(reverse=True)
        return to_remove
