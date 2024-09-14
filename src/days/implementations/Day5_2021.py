from src.days.IDay import IDay


class Day5_2021(IDay):

    def __init__(self, is_real_data):
        super().__init__()

        self.name: str = "day5"

        if is_real_data:
            self.input: str = f"src/days/implementations/inputs/2021/{self.name}.txt"
        else:
            self.input: str = f"src/days/tests/inputs/2021/{self.name}.txt"

        self.data: list[list[str]] = self.custom_import()

    def __str__(self) -> str:
        return f"{self.data[:2]} (...)"

    def custom_import(self) -> list[list[str]]:
        data: list[str] = self.import_string_data()
        result: list[list[str]] = []

        for line in data:
            temp: list[str] = line.split(" -> ")
            result.append(temp[0].split(",") + temp[1].split(","))

        return result

    def part1(self) -> int:
        position_dict: dict = {}
        count: int = 0

        for i in range(len(self.data)):
            x1: int = int(self.data[i][0])
            y1: int = int(self.data[i][1])
            x2: int = int(self.data[i][2])
            y2: int = int(self.data[i][3])

            if x1 == x2:
                position_dict = self.x1_eq_x2(position_dict, x1, y1, y2)
            elif y1 == y2:
                position_dict = self.y1_eq_y2(position_dict, y1, x1, x2)

        for key in position_dict.keys():
            if position_dict[key] > 1:
                count += 1
        return count

    def part2(self) -> int:
        position_dict: dict = {}
        count: int = 0

        for i in range(len(self.data)):
            x1: int = int(self.data[i][0])
            y1: int = int(self.data[i][1])
            x2: int = int(self.data[i][2])
            y2: int = int(self.data[i][3])

            if x1 == x2:
                position_dict = self.x1_eq_x2(position_dict, x1, y1, y2)
            elif y1 == y2:
                position_dict = self.y1_eq_y2(position_dict, y1, x1, x2)
            elif (x1 > x2) and (y1 > y2):
                position_dict = self.x1_bigger_y1_bigger(position_dict, x1, x2, y1, y2)
            elif (x1 < x2) and (y1 < y2):
                position_dict = self.x1_smaller_y1_smaller(
                    position_dict, x1, x2, y1, y2
                )
            elif (x1 > x2) and (y1 < y2):
                position_dict = self.x1_bigger_y1_smaller(position_dict, x1, x2, y1, y2)
            elif (x1 < x2) and (y1 > y2):
                position_dict = self.x1_smaller_y1_bigger(position_dict, x1, x2, y1, y2)

        for key in position_dict.keys():
            if position_dict[key] > 1:
                count += 1
        return count

    @staticmethod
    def x1_eq_x2(position_dict, x, y1, y2) -> dict:
        max_y: int = max(y1, y2)
        min_y: int = min(y1, y2)
        while max_y >= min_y:
            if (x, max_y) in position_dict.keys():
                position_dict[(x, max_y)] += 1
            else:
                position_dict[(x, max_y)] = 1
            max_y -= 1
        return position_dict

    @staticmethod
    def y1_eq_y2(position_dict, y1, x1, x2) -> dict:
        max_x: int = max(x1, x2)
        min_x: int = min(x1, x2)
        while max_x >= min_x:
            if (max_x, y1) in position_dict.keys():
                position_dict[(max_x, y1)] += 1
            else:
                position_dict[(max_x, y1)] = 1
            max_x -= 1
        return position_dict

    @staticmethod
    def x1_bigger_y1_bigger(position_dict, x1, x2, y1, y2) -> dict:
        while (x1 >= x2) and (y1 >= y2):
            if (x1, y1) in position_dict.keys():
                position_dict[(x1, y1)] += 1
            else:
                position_dict[(x1, y1)] = 1
            x1 -= 1
            y1 -= 1
        return position_dict

    @staticmethod
    def x1_smaller_y1_smaller(position_dict, x1, x2, y1, y2) -> dict:
        while (x2 >= x1) and (y2 >= y1):
            if (x2, y2) in position_dict.keys():
                position_dict[(x2, y2)] += 1
            else:
                position_dict[(x2, y2)] = 1
            x2 -= 1
            y2 -= 1
        return position_dict

    @staticmethod
    def x1_bigger_y1_smaller(position_dict, x1, x2, y1, y2) -> dict:
        while (x1 >= x2) and (y1 <= y2):
            if (x1, y1) in position_dict.keys():
                position_dict[(x1, y1)] += 1
            else:
                position_dict[(x1, y1)] = 1
            x1 -= 1
            y1 += 1
        return position_dict

    @staticmethod
    def x1_smaller_y1_bigger(position_dict, x1, x2, y1, y2) -> dict:
        while (x2 >= x1) and (y2 <= y1):
            if (x1, y1) in position_dict.keys():
                position_dict[(x1, y1)] += 1
            else:
                position_dict[(x1, y1)] = 1
            x1 += 1
            y1 -= 1
        return position_dict
