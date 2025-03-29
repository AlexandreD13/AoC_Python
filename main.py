import time
import pytest

from contextlib import redirect_stdout
from io import StringIO

from src import IDay

from src.implementations import (Day1_2015, Day2_2015, Day3_2015, Day4_2015, Day5_2015,
                                 Day6_2015, Day7_2015, Day8_2015, Day9_2015, Day10_2015)

from src.implementations import (Day1_2021, Day2_2021, Day3_2021, Day4_2021, Day5_2021,
                                 Day6_2021, Day7_2021, Day8_2021, Day9_2021, Day10_2021,
                                 Day11_2021)

from src.implementations import (Day1_2024, Day2_2024, Day3_2024)

years: dict = {
    "2015": [
        Day1_2015.Day1_2015(True),
        Day2_2015.Day2_2015(True),
        Day3_2015.Day3_2015(True),
        # Day4_2015.Day4_2015(True), # The naive method is costly
        Day5_2015.Day5_2015(True),
        # Day6_2015.Day6_2015(True), # The naive method is costly
        Day7_2015.Day7_2015(True),
        Day8_2015.Day8_2015(True),
        Day9_2015.Day9_2015(True),
        Day10_2015.Day10_2015(True),
    ],
    "2016": [],
    "2017": [],
    "2018": [],
    "2019": [],
    "2020": [],
    "2021": [
        Day1_2021.Day1_2021(True),
        Day2_2021.Day2_2021(True),
        Day3_2021.Day3_2021(True),
        Day4_2021.Day4_2021(True),  # Part 2 fails on tests for some reason
        Day5_2021.Day5_2021(True),
        Day6_2021.Day6_2021(True),
        Day7_2021.Day7_2021(True),
        Day8_2021.Day8_2021(True),
        Day9_2021.Day9_2021(True),
        Day10_2021.Day10_2021(True),
        # Day11_2021.Day11_2021(True),
    ],
    "2022": [],
    "2023": [],
    "2024": [
        Day1_2024.Day1_2024(True),
        Day2_2024.Day2_2024(True),
        Day3_2024.Day3_2024(True),
    ]
}


def main() -> None:
    total_year_time: float = 0
    total_time: float = 0

    for year, days in years.items():
        generate_year_header(year)

        for day in days:
            tests: list[str] = run_tests(day.name.capitalize(), year)
            generate_day_header(day)

            if len(day.data) > 0:
                start_time: float = time.time()

                run_real_data(day, tests)

                end_time: float = time.time() - start_time
                total_year_time += end_time

                print(f"\n\tTime taken:\t\t\t{end_time * 1000:.4f} ms")
            else:
                print(f"\tNo data in corresponding file")

        total_time += total_year_time
        print(f"\nTotal time taken ({year}):\t\t{total_year_time * 1000:.4f} ms")
        total_year_time = 0

    print(f"\n" + 124 * f"=")
    print(f"\nTotal time taken:\t\t\t{total_time * 1000:.4f} ms")
    print(f"\n" + 124 * f"=")


def generate_day_header(day) -> None:
    print(f"\n{day.name.capitalize()}")
    print(f"\tFilepath:\t\t\t{day.input}")


def generate_year_header(year) -> None:
    print(f"\n" + 60 * "=" + f" {year} " + 60 * f"=")


def run_real_data(day: IDay, tests: list[str]):
    print(f"\tImported data:\t\t\t{day}")

    part1_result: int = day.part1()
    part2_result: int = day.part2()

    print(
        f"\n\tResult of part 1 - Tests:\t"
        f"{"PASSED" if tests and "PASSED" in tests[0] else "FAILED"}"
    )
    print(f"\tResult of part 1:\t\t{part1_result} ({part1_result:,})")

    print(
        f"\n\tResult of part 2 - Tests:\t"
        f"{"PASSED" if tests and "PASSED" in tests[1] else "FAILED"}"
    )
    print(f"\tResult of part 2:\t\t{part2_result} ({part2_result:,})")


def run_tests(name: str, year: str) -> list[str]:
    f: StringIO = StringIO()

    with redirect_stdout(f):
        pytest.main(["-v", f"src/tests/{name}_{year}_test.py"])

    return [
        line for line in f.getvalue().splitlines() if "PASSED" in line or "FAILED" in line
    ]


if __name__ == "__main__":
    main()
