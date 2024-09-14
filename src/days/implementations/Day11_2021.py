from src.days.IDay import IDay


class Day11_2021(IDay):

    def __init__(self, is_real_data):
        super().__init__()

        self.name: str = "day11"

        if is_real_data:
            self.input: str = f"src/days/implementations/inputs/2021/{self.name}.txt"
        else:
            self.input: str = f"src/days/tests/inputs/2021/{self.name}.txt"

        self.data: list[str] = self.import_string_data()

        self.steps_p1: int = 100
        self.steps_p2: int = 0

    def __str__(self) -> str:
        return f"{self.data[:2]} (...)"

    def part1(self) -> int:
        return 0

    def part2(self) -> int:
        return 0
