from src.IDay import IDay


class Day2_2021(IDay):
    def __init__(self, is_real_data):
        super().__init__()

        self.name: str = "day2"
        self.year = "2021"

        if is_real_data:
            self.input: str = f"src/inputs/2021/{self.name}.txt"
        else:
            self.input: str = f"src/inputs/2021/{self.name}_test.txt"

        self.data: list[str] = self.import_string_data()

    def __str__(self) -> str:
        return f"{self.data[:5]} (...)"

    def part1(self) -> int:
        depth: int = 0
        horizontal: int = 0

        for index in range(len(self.data)):
            instruction, units = self.data[index].split()
            units: int = int(units)

            if instruction == "forward":
                horizontal += units
            elif instruction == "down":
                depth += units
            elif instruction == "up":
                depth -= units

        return horizontal * depth

    def part2(self) -> int:
        depth: int = 0
        horizontal: int = 0
        aim: int = 0

        for i in range(len(self.data)):
            instruction, units = self.data[i].split()
            units: int = int(units)

            if instruction == "forward":
                horizontal += units
                depth += aim * units
            elif instruction == "down":
                aim += units
            elif instruction == "up":
                aim -= units

        return horizontal * depth
