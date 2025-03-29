from typing import List

from src.IDay import IDay


class Day5_2015(IDay):
    def __init__(self, is_real_data):
        super().__init__()

        self.name = "day5"
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

        """

        count = 0
        for word in self.data:
            if self.has_3_vowels(word) and self.contains_double_string(word) and self.does_not_contain_strings(word):
                count += 1

        return count

    def part2(self) -> int:
        """

        """

        count = 0
        for word in self.data:
            if self.has_pair_2_letters(word) and self.has_duplicate_with_gap(word):
                count += 1

        return count

    @staticmethod
    def has_3_vowels(word: str) -> bool:
        """

        """

        count = 0
        for index in range(len(word)):
            if word[index] in "aeiou": count += 1

        return count >= 3

    @staticmethod
    def does_not_contain_strings(word: str) -> bool:
        """

        """

        if word.__contains__("ab") or word.__contains__("cd") or word.__contains__("pq") or word.__contains__("xy"):
            return False

        return True

    @staticmethod
    def contains_double_string(word: str) -> bool:
        """

        """

        for index in range(len(word) - 1):
            if word[index] == word[index + 1]:
                return True

        return False

    @staticmethod
    def has_pair_2_letters(word: str) -> bool:
        """

        """

        for index in range(len(word) - 1):
            if word[index:index + 2] in word[index + 2:]: return True

        return False

    @staticmethod
    def has_duplicate_with_gap(word: str) -> bool:
        """

        """

        for index in range(len(word) - 2):
            if word[index] == word[index + 2]: return True

        return False