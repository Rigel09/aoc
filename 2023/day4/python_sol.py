from pathlib import Path


def part1(file: Path) -> None:
    total: int = 0

    with file.open("r") as f:
        for line in f:
            winning_numbers = set(
                [int(x) for x in line.split(":")[1].strip().split("|")[0].strip().split()]
            )
            my_numbers = set(
                [int(x) for x in line.split(":")[1].strip().split("|")[1].strip().split()]
            )
            matches = winning_numbers.intersection(my_numbers)
            if matches:
                total += pow(2, len(matches) - 1)
            print(f"Matches: {matches} num: {len(matches)}  total: {total}")

    print(f"The total is: {total}")


if __name__ == "__main__":
    part1(Path("ex-pz-input.txt"))
    part1(Path("p1-pz-input.txt"))
