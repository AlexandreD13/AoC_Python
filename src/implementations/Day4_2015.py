import hashlib
import itertools
from typing import List

from src.IDay import IDay


class Day4_2015(IDay):
    def __init__(self, is_real_data):
        super().__init__()

        self.name = "day4"
        self.year = "2015"

        if is_real_data:
            self.input: str = f"src/inputs/2015/{self.name}.txt"
        else:
            self.input: str = f"src/inputs/2015/{self.name}_test.txt"

        self.data: str = self.import_string_data()[0]

    def __str__(self) -> str:
        return f"{self.data[:5]} (...)"

    def part1(self) -> int:
        """

        """

        return self.mine_adventcoin(leading_zeros=5)

    def part2(self) -> int:
        """

        """

        return self.mine_adventcoin(leading_zeros=6)

    def mine_adventcoin(self, leading_zeros: int) -> int:
        """

        """

        target = "0" * leading_zeros
        prefix = self.data.encode()

        for index in itertools.count():
            result = hashlib.md5(prefix + str(index).encode()).hexdigest()
            if result.startswith(target):
                return index