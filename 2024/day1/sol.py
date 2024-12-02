from pathlib import Path

import numpy as np


def run(file: Path) -> None:
    lines: list[str] = []

    with file.open("r", encoding="utf8") as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    left_col: list[int] = []
    right_col: list[int] = []

    for line in lines:
        vals = line.split()
        left_col.append(int(vals[0]))
        right_col.append(int(vals[-1]))

    left_col.sort()
    right_col.sort()

    left = np.array(left_col)
    right = np.array(right_col)

    print(f"ans: {np.sum(np.abs( right - left ))}")


if __name__ == "__main__":
    run(Path("./example_input.txt"))
    run(Path("./puzzle-input.txt"))
