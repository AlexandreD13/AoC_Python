from typing import List

from src.IDay import IDay


class Day2_2015(IDay):
    def __init__(self, is_real_data):
        super().__init__()

        self.name = "day2"
        self.year = "2015"

        if is_real_data:
            self.input: str = f"src/inputs/2015/{self.name}.txt"
        else:
            self.input: str = f"src/inputs/2015/{self.name}_test.txt"

        self.data: List[str] = self.import_string_data()

    def __str__(self) -> str:
        return f"{self.data[:5]} (...)"

    def part1(self) -> int:
        """
        Calculates the total wrapping paper required for a list of presents.

        Each present's wrapping paper is calculated as:
            2 * (lw + wh + hl) + min(lw, wh, hl)
        where:
            - lw = length * width
            - wh = width * height
            - hl = height * length
            - min(lw, wh, hl) is the smallest face area, which represents the extra paper.

        Returns:
            int: The total square feet of wrapping paper needed.

        Time Complexity:
            O(N), where N is the number of presents. Each line is split, mapped to integers,
            three multiplications and additions are performed, and the min() function runs in O(1).
            Thus, the overall complexity is O(N).
        """

        total = 0
        for line in self.data:
            length, width, height = map(int, line.split("x"))
            lw, wh, hl = length * width, width * height, height * length
            total += 2 * (lw + wh + hl) + min(lw, wh, hl)

        return total

    def part2(self) -> int:
        """
        Calculates the total ribbon required for a list of presents.

        Each present's ribbon is calculated as:
            2 * (smallest perimeter) + (volume)
        where:
            - The smallest perimeter is from the two shortest sides.
            - The volume is length * width * height.

        Returns:
            int: The total feet of ribbon needed.

        Time Complexity:
            O(N), where N is the number of presents. Each line is split, mapped to integers,
            sorted (O(1) for 3 elements), and a few arithmetic operations are performed.
            Thus, the overall complexity is O(N).
        """

        total = 0
        for line in self.data:
            length, width, height = sorted(map(int, line.split("x")))
            total += 2 * (length + width) + (length * width * height)

        return total