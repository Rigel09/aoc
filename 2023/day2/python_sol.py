from pathlib import Path
from typing import List


class Round:
    def __init__(self, red: int = 0, green: int = 0, blue: int = 0) -> None:
        self.red = red
        self.green = green
        self.blue = blue


class Game:
    def __init__(self, game_str: str) -> None:
        self.game = int(game_str.split(":")[0][5:])
        self.rounds: List[Round] = []

        for rnd_str in game_str.split(":")[1].split(";"):
            self.rounds.append(Round())
            for clr_set in rnd_str.strip().split(","):
                num, color = clr_set.split()
                setattr(self.rounds[-1], color.strip(), int(num.strip()))

    @property
    def max_red(self) -> int:
        return max(rnd.red for rnd in self.rounds)

    @property
    def max_blue(self) -> int:
        return max(rnd.blue for rnd in self.rounds)

    @property
    def max_green(self) -> int:
        return max(rnd.green for rnd in self.rounds)

    def is_valid_game(self, red_total: int, blue_total: int, green_total: int) -> bool:
        return (
            self.max_green <= green_total
            and self.max_red <= red_total
            and self.max_blue <= blue_total
        )


def part1(file: Path, red_total: int, blue_total: int, green_total: int) -> None:
    games: List[Game] = []
    with file.open("r", encoding="utf8") as f:
        for line in f:
            if not line:
                continue

            game = Game(line.strip())
            if game.is_valid_game(red_total, blue_total, green_total):
                games.append(game)

    game_id_sum = sum(g.game for g in games)
    print(f"Part 1 result for {file} is {game_id_sum}")


def part2(file: Path) -> None:
    power_sum: int = 0
    with file.open("r", encoding="utf8") as f:
        for line in f:
            if not line:
                continue

            game = Game(line.strip())
            power_sum += game.max_red * game.max_blue * game.max_green

    print(f"Part 2 result for {file} is {power_sum}")


if __name__ == "__main__":
    part1(Path("ex-pz-input.txt"), red_total=12, blue_total=14, green_total=13)
    part1(Path("p1-pz-input.txt"), red_total=12, blue_total=14, green_total=13)  # 2149
    part2(Path("ex-pz-input.txt"))
    part2(Path("p1-pz-input.txt"))
