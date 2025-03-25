from src.IDay import IDay


class Day1_2015(IDay):
    def __init__(self, is_real_data):
        super().__init__()

        self.name = "day1"
        self.year = "2015"

        if is_real_data:
            self.input: str = f"src/inputs/2015/{self.name}.txt"
        else:
            self.input: str = f"src/inputs/2015/{self.name}_test.txt"

        self.data: str = self.import_string_data()[0]

    def __str__(self) -> str:
        return f"'{self.data[:50]}' (...)"

    def part1(self) -> int:
        """
        Calculates the difference between the number of '(' and ')' characters in the input string.

        Returns:
            int: The net count of '(' minus ')', representing the final floor.

        Time Complexity:
            O(N), where N is the length of `self.data`. The method counts occurrences of '(' and ')'
            separately, both taking O(N) time, leading to an overall O(N) complexity.
        """

        return self.data.count("(") - self.data.count(")")

    def part2(self) -> int:
        """
        Determines the first position (1-based index) where the running total reaches -1.

        Returns:
            int: The index at which the total first becomes -1.

        Time Complexity:
            O(N), where N is the length of `self.data`. The loop iterates through the string once,
            making a single pass, resulting in a linear time complexity.
        """

        total = 0
        for index, char in enumerate(self.data, start=1):
            total += 1 if char == "(" else -1
            if total == -1:
                return index