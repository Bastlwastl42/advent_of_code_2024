from pathlib import Path
from utils.file import readin_files
import re


def find_all_XMAS(line: str) -> int:
    """file content is separated by spaces"""
    matches = re.findall(r'XMAS', line)
    return len(matches)


def find_all_MAS(line: str):
    return re.finditer(r'MAS', line)


def parse_linewise_back_and_forth(lines: list[str]) -> int:
    total_result = 0
    for line in lines:
        act_line = line
        total_result += find_all_XMAS(act_line)
        reversed_lined = act_line[::-1]
        total_result += find_all_XMAS(reversed_lined)
    return total_result


def toplefttobottomright(file_content):
    toplefttoright: list[str] = []
    max_row = len(file_content)
    max_col = len(file_content[0])
    # point is (row,col)
    starting_tuples = [(counter, 0) for counter in range(max_row)]
    starting_tuples.extend([(0, counter) for counter in range(1, max_col)])
    for point in starting_tuples:
        act_str = ''
        step_counter = 0
        limit = min(max_row - point[0], max_col - point[1])
        while step_counter < limit:
            act_str += file_content[point[0] + step_counter][point[1] + step_counter]
            step_counter += 1
        toplefttoright.append(act_str.strip())
    return toplefttoright


def bottomlefttotopright(file_content):
    max_row = len(file_content)
    max_col = len(file_content[0])
    ret_val: list[str] = []
    starting_tuples = [(max_row - 1, counter) for counter in range(max_col)]
    starting_tuples.extend([(counter, 0) for counter in range(0, max_row - 1)])
    for point in starting_tuples:
        act_str = ''
        step_counter = 0
        while (point[0] - step_counter) >= 0 and (point[1] + step_counter) < max_col:
            act_str += file_content[point[0] - step_counter][point[1] + step_counter]
            step_counter += 1
        ret_val.append(act_str.strip())

    return ret_val


def day_four_part_one(input_file: str, input_path: Path) -> int:
    """x-mas wortsuche"""
    file_content = readin_files(input_file, input_path)
    file_content = [line.strip() for line in file_content]
    total_result = 0

    # slice left to right and right to left
    total_result += parse_linewise_back_and_forth(file_content)

    # top to bottom and bottom to top
    # mirror diagonal
    top_bottom: list[str] = []
    for row_counter in range(len(file_content[0])):
        act_str = ''
        for counter in range(len(file_content)):
            act_str += file_content[counter][row_counter]
        top_bottom.append(act_str.strip())
    total_result += parse_linewise_back_and_forth(top_bottom)

    # top left corner to lower right corner
    toplefttoright: list[str] = toplefttobottomright(file_content)

    total_result += parse_linewise_back_and_forth(toplefttoright)

    bottomlefttoright = bottomlefttotopright(file_content)
    total_result += parse_linewise_back_and_forth(bottomlefttoright)

    return total_result


def day_four_part_two(input_file, input_path: Path = Path.cwd()) -> int:
    """mas in xform pattern search"""
    file_content = readin_files(input_file, input_path)
    file_content = [line.strip() for line in file_content]
    # top left corner to lower right corner
    total_match_counter = 0

    max_row = len(file_content)
    max_col = len(file_content[0])
    # get all non-border points
    all_points: list[tuple[int, int]] = []
    for col_counter in range(1, max_col - 1):
        for row_counter in range(1, max_row - 1):
            all_points.append((row_counter, col_counter))

    for point in all_points:
        if file_content[point[0]][point[1]] != 'A':
            continue
        # get surrounding pattern
        top_left = file_content[point[0] - 1][point[1] - 1]
        top_right = file_content[point[0] - 1][point[1] + 1]
        bottom_left = file_content[point[0] + 1][point[1] - 1]
        bottom_right = file_content[point[0] + 1][point[1] + 1]
        direction_grave = False
        direction_deque = False
        if any([x in ['X', 'A'] for x in [top_right, top_left, bottom_right, bottom_left]]):
            continue

        if (top_left == 'M' and bottom_right == 'S') or (top_left == 'S' and bottom_right == 'M'):
            direction_grave = True

        if (top_right == 'M' and bottom_left == 'S') or (top_right == 'S' and bottom_left == 'M'):
            direction_deque = True

        if direction_grave and direction_deque:
            total_match_counter += 1

    return total_match_counter


if __name__ == "__main__":
    my_input_path = Path.cwd() / 'assets'
    print(day_four_part_one('input.txt', my_input_path))
    print(day_four_part_two('input.txt', my_input_path))
