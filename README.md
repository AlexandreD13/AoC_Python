# Advent Of Code

**Language:** Python 3.12

---

## Run code

```bash
python main.py
```

## Reformat code

```bash
python -m black .\src\

# python -m black .\main.py .\src\
```

## Class template

```python
from src.IDay import IDay


class Day1_2015(IDay):
    def __init__(self, is_real_data):
        super().__init__()

        self.name = "day1"
        self.year = "2015"

        if is_real_data:
            self.input: str = f"src/inputs/2015/{self.name}.txt"
        else:
            self.input: str = f"src/inputs/2015/{self.name}_test.txt"

        self.data: str = self.import_string_data()[0]

    def __str__(self) -> str:
        return ""
    
    def part1(self) -> int | str:
        pass

    def part2(self) -> int | str:
        pass
```