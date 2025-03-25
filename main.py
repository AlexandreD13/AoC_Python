import time
import pytest

from contextlib import redirect_stdout
from io import StringIO
from typing import Callable

from src.Color import Color
from src import IDay
from src.implementations import (
    Day1_2021,
    Day2_2021,
    Day3_2021,
    Day4_2021,
    Day5_2021,
    Day6_2021,
    Day7_2021,
    Day8_2021,
    Day9_2021,
    Day10_2021,
    Day11_2021,

    Day1_2024,
    Day2_2024,
    Day3_2024
)

days: [Callable] = [
    # 2021
    Day1_2021.Day1_2021(True),
    Day2_2021.Day2_2021(True),
    Day3_2021.Day3_2021(True),
    Day4_2021.Day4_2021(True),  # Part 2 test is failing
    Day5_2021.Day5_2021(True),
    Day6_2021.Day6_2021(True),
    Day7_2021.Day7_2021(True),
    Day8_2021.Day8_2021(True),
    Day9_2021.Day9_2021(True),
    Day10_2021.Day10_2021(True),
    # Day11_2021.Day11_2021(True),

    # 2024
    Day1_2024.Day1_2024(True),
    Day2_2024.Day2_2024(True),
    Day3_2024.Day3_2024(True),
]


def main() -> None:
    total_time: float = 0
    
    for day in days:
        tests: list[str] = run_tests(day.name.capitalize(), year)

        print(f"\n{Color.GREEN}{Color.BOLD}{day.name.capitalize()}{Color.END}")
        print(f"\tFilepath:\t\t\t\t\t{Color.BLUE}{Color.BOLD}{day.input}{Color.END}")

        if len(day.data) > 0:
            start_time: float = time.time()

            run_real_data(day, tests)

            end_time: float = time.time() - start_time
            total_time += end_time

            print(
                f"\tTime taken:\t\t\t\t\t{Color.BLUE}{Color.BOLD}{end_time * 1000:.4f} ms{Color.END}"
            )
        else:
            print(
                f"\t{Color.RED}{Color.BOLD}No data in corresponding file{Color.END}{Color.END}"
            )

    print(
        f"\n{Color.GREEN}{Color.BOLD}Total Time taken:\t\t\t\t{total_time * 1000:.4f} ms{Color.END}\n"
    )


def run_real_data(day: IDay, tests: list[str]):
    print(f"\tImported data:\t\t\t\t{Color.BLUE}{Color.BOLD}{day}{Color.END}")
    part1_result: int = day.part1()
    part2_result: int = day.part2()
    print(
        f"\tResult of part 1 - Tests:\t"
        f"{Color.BLUE}{Color.BOLD}{"PASSED" if tests and "PASSED" in tests[0] else "FAILED"}{Color.END}"
    )
    print(f"\tResult of part 1:\t\t\t{Color.BLUE}{Color.BOLD}{part1_result} ({part1_result:,}){Color.END}")
    print(
        f"\tResult of part 2 - Tests:\t"
        f"{Color.BLUE}{Color.BOLD}{"PASSED" if tests and "PASSED" in tests[1] else "FAILED"}{Color.END}"
    )
    print(f"\tResult of part 2:\t\t\t{Color.BLUE}{Color.BOLD}{part2_result} ({part2_result:,}){Color.END}")


def run_tests(name: str, year: str) -> list[str]:
    f: StringIO = StringIO()

    with redirect_stdout(f):
        pytest.main(["-v", f"src/tests/{name}_{year}_test.py"])

    return [
        line for line in f.getvalue().splitlines() if "PASSED" in line or "FAILED" in line
    ]


if __name__ == "__main__":
    main()
