from src.IDay import IDay


class Day2_2024(IDay):

    def __init__(self, is_real_data):
        super().__init__()

        self.name = "day2"
        self.year = "2024"

        if is_real_data:
            self.input: str = f"src/inputs/2024/{self.name}.txt"
        else:
            self.input: str = f"src/inputs/2024/{self.name}_test.txt"

        self.data: list[str] = self.import_string_data()

    def __str__(self) -> str:
        return f"{self.data[:3]} (...)"

    @staticmethod
    def parse_line(line: str) -> list[int]:
        return [int(elem) for elem in line.split(" ")]

    @staticmethod
    def is_safe(line: list[int]) -> bool:
        pairs = list(zip(line, line[1:]))

        is_increasing = all(a <= b for a, b in pairs)
        is_decreasing = all(a >= b for a, b in pairs)
        valid_differences = all(1 <= abs(a - b) <= 3 for a, b in pairs)

        return (is_increasing or is_decreasing) and valid_differences

    def can_be_safe_by_removing_one(self, line: list[int]) -> bool:
        n = len(line)
        for i in range(n):
            if 0 < i < n - 1:
                if abs(line[i - 1] - line[i + 1]) > 3:
                    continue

            modified_line = line[:i] + line[i + 1:]
            if self.is_safe(modified_line):
                return True

        return False

    def part1(self) -> int:
        safe_count = 0
        for line in self.data:
            line_values = self.parse_line(line)

            if self.is_safe(line_values):
                safe_count += 1

        return safe_count

    def part2(self) -> int:
        safe_count = 0
        for line in self.data:
            line_values = self.parse_line(line)

            if self.is_safe(line_values) or self.can_be_safe_by_removing_one(line_values):
                safe_count += 1

        return safe_count
