import sys

from src.IDay import IDay


class Day8_2021(IDay):

    def __init__(self, is_real_data):
        super().__init__()

        self.name = "day8"
        self.year = "2021"

        if is_real_data:
            self.input: str = f"src/inputs/2021/{self.name}.txt"
        else:
            self.input: str = f"src/inputs/2021/{self.name}_test.txt"

        self.data: (list[list[str]], list[list[str]]) = self.custom_import()

    def __str__(self) -> str:
        return f"([Input (...)], [Output (...)])"

    def custom_import(self) -> (list[list[str]], list[list[str]]):
        data: list[str] = self.import_string_data()
        input_data: list[list[str]] = []
        output_data: list[list[str]] = []

        try:
            for i in range(len(data)):
                input_data.append(data[i].split("|")[0].split())
                output_data.append(data[i].split("|")[1].split())

            return input_data, output_data
        except IndexError:
            sys.exit(1)

    def part1(self) -> int:
        counter: int = 0

        for line in self.data[1]:
            for item in line:
                if len(item) in [2, 3, 4, 7]:
                    counter += 1

        return counter

    def part2(self) -> int:
        values_list: list[dict] = self.parse_line()
        line: int = 0
        total: int = 0

        for line_dict in values_list:
            total += self.decipher_output(line_dict, self.data[1][line])
            line += 1

        return total

    def parse_line(self) -> list[dict]:
        values_list: list[dict] = []

        for line in self.data[0]:
            line.sort(key=len)
            values_dict: dict = self.identify_values(line)
            values_list.append(values_dict)

        return values_list

    def identify_values(self, line: str) -> dict:
        values_dict: dict = {
            0: "",
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: "",
            8: "",
            9: "",
        }

        for item in line:
            match len(item):
                case 2:
                    values_dict[1] = item
                case 3:
                    values_dict[7] = item
                case 4:
                    values_dict[4] = item
                case 5:
                    values_dict = self.len5(values_dict, item)
                case 6:
                    values_dict = self.len6(values_dict, item)
                case _:
                    values_dict[8] = item

        return values_dict

    @staticmethod
    def len5(values_dict: dict, item: str) -> dict:
        if set(values_dict[1]).issubset(set(item)):
            values_dict[3] = item
        else:
            temp: list[str] = list(item)

            for letter in values_dict[4]:
                if letter in temp:
                    del temp[temp.index(letter)]

            if len(temp) == 2:
                values_dict[5] = item
            else:
                values_dict[2] = item

        return values_dict

    @staticmethod
    def len6(values_dict: dict, item: str) -> dict:
        if set(values_dict[1]).issubset(set(item)):
            if set(values_dict[4]).issubset(set(item)):
                values_dict[9] = item
            else:
                values_dict[0] = item
        else:
            values_dict[6] = item

        return values_dict

    @staticmethod
    def decipher_output(input_line: dict, output_line: str):
        output_total: str = ""

        for output_item in output_line:
            for key, value in input_line.items():
                if set(value) == set(output_item):
                    output_total += str(key)

        return int(output_total)
