from abc import ABC, abstractmethod

import os
from typing import Any


class IDay(ABC):
    input: str

    def __init__(self):
        pass

    def import_integer_data(self) -> list[int]:
        if os.path.exists(self.input):
            with open(self.input, "r") as file:
                return [int(line) for line in file]
        else:
            raise FileExistsError(f"File '{self.input}' does not exist.")

    def import_string_data(self) -> list[str]:
        if os.path.exists(self.input):
            with open(self.input, "r") as file:
                return [line.strip("\n") for line in file]
        else:
            raise FileExistsError(f"File '{self.input}' does not exist.")

    def custom_import(self) -> Any:
        pass

    @abstractmethod
    def part1(self) -> int | str:
        pass

    @abstractmethod
    def part2(self) -> int | str:
        pass
