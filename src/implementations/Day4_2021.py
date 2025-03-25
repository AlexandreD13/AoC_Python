from src.IDay import IDay


class Board:
    def __init__(self):
        self.board: list[list[int]] = []

    def __str__(self) -> str:
        return f"{self.board}"

    def check_for_bingo(self, numbers: list[int]) -> bool:
        for row in self.board:
            has_bingo = self.contains_all_elements(numbers, row)

            if has_bingo:
                return True

        for i in range(len(self.board) - 1):
            column: list[int] = [
                self.board[0][i],
                self.board[1][i],
                self.board[2][i],
                self.board[3][i],
                self.board[4][i],
            ]

            has_bingo = self.contains_all_elements(numbers, column)

            if has_bingo:
                return True

        return False

    def calculate_undrawn_sum(self, numbers: list[int]) -> int:
        array: list[int] = []

        for strings in self.board:
            array.append(strings[0])
            array.append(strings[1])
            array.append(strings[2])
            array.append(strings[3])
            array.append(strings[4])

        undrawn: list[int] = self.remove_common_elements(array, numbers)

        total: int = 0
        for value in undrawn:
            total += int(value)

        return total

    @staticmethod
    def contains_all_elements(array1: list[int], array2: list[int]) -> bool:
        array1_set: set = set(array1)

        for value in array2:
            if value not in array1_set:
                return False

        return True

    @staticmethod
    def remove_common_elements(array1: list[int], array2: list[int]) -> list[int]:
        array2_set: set = set(array2)
        result: list[int] = []

        for value in array1:
            if value not in array2_set:
                result.append(value)

        return result


class Day4_2021(IDay):

    def __init__(self, is_real_data):
        super().__init__()

        self.name = "day4"
        self.year = "2021"

        if is_real_data:
            self.input: str = f"src/inputs/2021/{self.name}.txt"
        else:
            self.input: str = f"src/inputs/2021/{self.name}_test.txt"

        self.data: (list[str], [Board]) = self.custom_import()

    def __str__(self) -> str:
        return f"({self.data[0][0:5]} (...), [Board 1 (...)])"

    def custom_import(self) -> (list[str], list[Board]):
        data = self.import_string_data()
        numbers: list[int] = []
        boards: list[Board] = []
        board: Board = Board()

        for line in data:
            if len(numbers) == 0:
                line = line.split(",")
                numbers = [int(x) for x in line]
            else:
                if line == "":
                    if len(board.board) > 0:
                        boards.append(board)
                        board = Board()
                else:
                    line = line.strip().split(" ")
                    line = [int(x) for x in line if x]
                    board.board.append(line)

        boards.append(board)
        return numbers, boards

    def part1(self) -> int:
        index: int = 5

        while True:
            subset: list[str] = self.data[0][:index]

            for board in self.data[1]:
                has_bingo = board.check_for_bingo(subset)

                if has_bingo:
                    return subset[-1] * board.calculate_undrawn_sum(subset)

            index += 1

    def part2(self) -> int:
        index: int = 5
        has_bingo: list[int] = []

        while index < len(self.data[0]) - 1:
            subset: list[int] = self.data[0][:index]

            for i in range(len(self.data[1])):
                if self.data[1][i].check_for_bingo(subset) and i not in has_bingo:
                    has_bingo.append(i)

                if len(self.data[1]) - 1 == len(has_bingo):
                    return subset[-1] * self.data[1][i].calculate_undrawn_sum(subset)

            index += 1
