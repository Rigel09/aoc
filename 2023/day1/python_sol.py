"""
This file solves the first puzzles for Day 1 of advent of code
"""

import re
from pathlib import Path
from typing import List


def part_1(file: Path) -> None:
    # Example solution is 77

    expression = re.compile("[^0-9]")
    values: List[int] = []
    with file.open("r", encoding="utf8") as f:
        for line in f:
            new_line = expression.sub("", line)
            values.append(int(new_line[0] + new_line[-1]))

    print(f"The sum for {file} for part 1 is {sum(values)}")


def part_2(file: Path) -> None:
    # Example solution is 281
    int_list = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    total_value: int = 0
    with file.open("r", encoding="utf8") as f:
        for line in f:
            numbers: List[str] = []
            idx: int = 0
            while idx < len(line):
                try:
                    int(line[idx])
                    numbers.append(line[idx])
                except ValueError:
                    for val, str_int in enumerate(int_list):
                        if str_int == line[idx : idx + len(str_int)]:
                            numbers.append(str(val))
                            break

                idx += 1

            total_value += int(numbers[0] + numbers[-1])
    print(f"The total sum for {file} is {total_value}")


if __name__ == "__main__":
    part_1(Path("example-puzzle-input.txt"))
    part_1(Path("puzzle-input.txt"))
    print()
    part_2(Path("example-puzzle-input-p2.txt"))
    part_2(Path("puzzle-input.txt"))
