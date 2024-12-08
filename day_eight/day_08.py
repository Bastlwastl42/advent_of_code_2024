from pathlib import Path
from utils.file import readin_files
from itertools import combinations


def prime_factors(n: int) -> list[int]:
    if 4 > n > 0:
        return [n]
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def get_antena_positions_from_file(file_content) -> dict[str, list[tuple[int, int]]]:
    ret_antena_dict: dict[str, list[tuple[int, int]]] = {}
    for row_counter, line in enumerate(file_content):
        for col_counter, val in enumerate(line.strip()):
            if val == '.':
                continue
            if val in ret_antena_dict.keys():
                ret_antena_dict[val].append((row_counter, col_counter))
            else:
                ret_antena_dict[val] = [(row_counter, col_counter)]
    return ret_antena_dict


def dist_vec(p1: tuple[int, int], p2: tuple[int, int]) -> tuple[int, int]:
    """get vec between two points"""
    return p2[0] - p1[0], p2[1] - p1[1]


def simplify_vec(vec: tuple[int, int]) -> tuple[int, int]:
    prime_fak_one = prime_factors(abs(vec[0]))
    prime_fak_two = prime_factors(abs(vec[1]))
    if len(prime_fak_one) == 1 or len(prime_fak_two) == 1:
        return vec
    for fak in sorted(prime_fak_one):
        if fak in prime_fak_two:
            return vec[0] / fak, vec[1] / fak
    return vec


def revert_vec(vec: tuple[int, int]) -> tuple[int, int]:
    """revert vector"""
    return vec[0] * -1, vec[1] * -1


def point_add_vec(point: tuple[int, int], vec: tuple[int, int]) -> tuple[int, int]:
    """apply vector to a point"""
    return point[0] + vec[0], point[1] + vec[1]


def point_inside_grid(point: tuple[int, int], max_row: int, max_col: int) -> bool:
    return not (point[0] < 0 or point[1] < 0 or point[0] >= max_row or point[1] >= max_col)


def part_one(input_file: str, input_path: Path) -> int:
    """some linalg, why not :)"""
    file_content = readin_files(input_file, input_path)
    max_row = len(file_content)
    max_col = len(file_content[0]) - 1  # remove that newline char for calculations
    antena_dict = get_antena_positions_from_file(file_content)
    all_points: set[tuple[int, int]] = set()
    for freq, positions in antena_dict.items():
        for ant_pair in combinations(positions, 2):
            dist = dist_vec(ant_pair[0], ant_pair[1])
            rev_dist = revert_vec(dist)
            node_one = point_add_vec(ant_pair[1], dist)
            node_two = point_add_vec(ant_pair[0], rev_dist)
            if point_inside_grid(node_one, max_row, max_col):
                all_points.add(node_one)
            if point_inside_grid(node_two, max_row, max_col):
                all_points.add(node_two)
    return len(all_points)


def part_two(input_file, input_path: Path = Path.cwd()) -> int:
    file_content = readin_files(input_file, input_path)
    max_row = len(file_content)
    max_col = len(file_content[0]) - 1  # remove that newline char for calculations
    antena_dict = get_antena_positions_from_file(file_content)
    all_points: set[tuple[int, int]] = set()
    for freq, positions in antena_dict.items():
        for ant_pair in combinations(positions, 2):
            dist = dist_vec(ant_pair[0], ant_pair[1])
            short_dist = simplify_vec(dist)
            # start at first antena and move in one dir, then revert, rinse and repeat
            next_point = ant_pair[0]
            while point_inside_grid(next_point, max_row, max_col):
                all_points.add(next_point)
                next_point = point_add_vec(next_point, short_dist)
            next_point = ant_pair[0]
            rev_short_dist = revert_vec(short_dist)
            while point_inside_grid(next_point, max_row, max_col):
                all_points.add(next_point)
                next_point = point_add_vec(next_point, rev_short_dist)

    return len(all_points)


if __name__ == "__main__":
    my_input_path = Path.cwd() / 'assets'
    print(part_one('input.txt', my_input_path))
    print(part_two('input.txt', my_input_path))
