from src.IDay import IDay

from queue import LifoQueue


class Day10_2021(IDay):

    def __init__(self, is_real_data):
        super().__init__()

        self.name = "day10"
        self.year = "2021"

        if is_real_data:
            self.input: str = f"src/inputs/2021/{self.name}.txt"
        else:
            self.input: str = f"src/inputs/2021/{self.name}_test.txt"

        self.data: list[str] = self.import_string_data()

    def __str__(self) -> str:
        return f"{self.data[:1]} (...)"

    def part1(self) -> int:
        total: int = 0
        cost: dict = {")": 3, "]": 57, "}": 1197, ">": 25137}

        for i in range(len(self.data)):
            lifo_queue: LifoQueue = LifoQueue()

            for character in self.data[i]:
                if lifo_queue.empty() or character not in ")]}>":
                    lifo_queue.put(character)
                else:
                    top: str = lifo_queue.get()
                    if (
                        (
                            (
                                top == "("
                                and character != ")"
                                or top == "["
                                and character != "]"
                            )
                            or top == "{"
                            and character != "}"
                        )
                        or top == "<"
                        and character != ">"
                    ):
                        total += cost[character]
                        break

        return total

    def part2(self) -> int:
        totals: list[int] = []
        to_remove: list[int] = []

        for i in range(len(self.data)):
            lifo_queue: LifoQueue = LifoQueue()
            self.find_corrupted_lines(i, lifo_queue, to_remove)
            totals.append(self.find_total_p2(lifo_queue))

        self.remove_corrupted_lines(to_remove, totals)
        totals.sort()

        return totals[len(totals) // 2]

    @staticmethod
    def remove_corrupted_lines(to_remove: list[int], totals: list[int]) -> None:
        for index in sorted(to_remove, reverse=True):
            if 0 <= index < len(totals):
                totals.pop(index)

    @staticmethod
    def find_total_p2(lifo_queue: LifoQueue) -> int:
        total: int = 0

        while not lifo_queue.empty():
            top: str = lifo_queue.get()

            if top == "(":
                total *= 5
                total += 1
            elif top == "[":
                total *= 5
                total += 2
            elif top == "{":
                total *= 5
                total += 3
            else:
                total *= 5
                total += 4

        return total

    def find_corrupted_lines(
        self, i: int, lifo_queue: LifoQueue, to_remove: list[int]
    ) -> None:
        for character in self.data[i]:
            if lifo_queue.empty() or character not in ")]}>":
                lifo_queue.put(character)
            else:
                top: str = lifo_queue.get()

                if (
                    (
                        (
                            top == "("
                            and character != ")"
                            or top == "["
                            and character != "]"
                        )
                        or top == "{"
                        and character != "}"
                    )
                    or top == "<"
                    and character != ">"
                ):
                    to_remove.append(i)
