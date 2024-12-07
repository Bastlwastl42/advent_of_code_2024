from pathlib import Path
from utils.file import readin_files
import re


def find_all_valid_mul_commands(file_content: str) -> list[str]:
    """file content is separated by spaces"""
    matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)', file_content)

    return [x[4:-1].split(',') for x in matches]

def find_do_and_dont_in_input(input_string: str) -> list:
    do_matches = re.split(r'do\(\)', input_string)
    final_list = ''
    for match in do_matches:
        dont_matches = re.split(r'don\'t\(\)', match, maxsplit=1)
        final_list+=dont_matches[0]

    return find_all_valid_mul_commands(final_list)

def day_three_part_one(input_file: str, input_path: Path) -> int:
    """solving puzzle one for day one: sorted distances"""
    file_content = readin_files(input_file, input_path)
    merged_input = ''
    for line in file_content:
        merged_input += line
    all_matches = find_all_valid_mul_commands(merged_input)
    total_result = 0
    for match in all_matches:
        total_result += int(match[0]) * int(match[1])
    return total_result


def day_three_part_two(input_file, input_path: Path = Path.cwd()) -> int:
    """doing sliding window differentiation"""
    file_content = readin_files(input_file, input_path)
    merged_input = ''
    for line in file_content:
        merged_input += line
    all_matches = find_do_and_dont_in_input(merged_input)
    total_result = 0
    for match in all_matches:
        total_result += int(match[0]) * int(match[1])
    return total_result


if __name__ == "__main__":
    my_input_path = Path.cwd() / 'assets'
    print(day_three_part_one('input.txt', my_input_path))
    print(day_three_part_two('input.txt', my_input_path))
