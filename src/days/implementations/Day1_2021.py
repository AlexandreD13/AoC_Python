from src.days.IDay import IDay


class Day1_2021(IDay):

    def __init__(self, is_real_data):
        super().__init__()

        self.name: str = "day1"

        if is_real_data:
            self.input: str = f"src/days/implementations/inputs/2021/{self.name}.txt"
        else:
            self.input: str = f"src/days/tests/inputs/2021/{self.name}.txt"

        self.data: list[int] = self.import_integer_data()

    def __str__(self) -> str:
        return f"{self.data[:5]} (...)"

    def part1(self) -> int:
        count: int = 0

        for index in range(0, len(self.data) - 1):
            if self.data[index + 1] > self.data[index]:
                count += 1

        return count

    def part2(self) -> int:
        count: int = 0

        for index in range(2, len(self.data) - 1):
            window_a: int = (
                self.data[index - 2] + self.data[index - 1] + self.data[index]
            )
            window_b: int = (
                self.data[index - 1] + self.data[index] + self.data[index + 1]
            )

            if window_b > window_a:
                count += 1

        return count
