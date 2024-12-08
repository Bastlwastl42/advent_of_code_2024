from pathlib import Path
from utils.file import readin_files


class Tile:
    x: int
    y: int
    is_obstacle: bool
    is_visited: bool

    def visited(self):
        self.is_visited = True

    def nextMove(self, dx: int, dy: int) -> (int, int):
        return self.x + dx, self.y + dy


def part_one(input_file: str, input_path: Path) -> int:
    """solving puzzle one for day one: sorted distances"""
    file_content = readin_files(input_file, input_path)
    fullmap: dict[tuple(int, int), Tile] = {}
    for x_counter, line in enumerate(file_content):
        for y_counter,  spot in enumerate(line):
            if spot == '.':
                # normal tile, just create
                fullmap[x_counter, y_counter]
    return 0


def part_two(input_file, input_path: Path = Path.cwd()) -> int:
    return 0


if __name__ == "__main__":
    my_input_path = Path.cwd() / 'assets'
    print(part_one('input.txt', my_input_path))
    print(part_two('input.txt', my_input_path))
