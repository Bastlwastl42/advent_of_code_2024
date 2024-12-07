from pathlib import Path
from typing import List

from utils.file import readin_files


def convert_list_to_numbered_list(file_content: list):
    """file content is separated by spaces"""
    list_one: list = []
    list_two: list = []
    for line in file_content:
        numbers = line.split("   ")
        list_one.append(int(numbers[0]))
        list_two.append(int(numbers[1]))

    return list_one, list_two


def convert_list_to_occourence_dict(input_list: list):
    """generate a dict of occourences"""
    ret_dict: dict = {}
    for value in input_list:
        if value in ret_dict.keys():
            ret_dict[value] += 1
        else:
            ret_dict[value] = 1
    return ret_dict


def day_one_part_one(input_file: str, input_path: Path):
    """solving puzzle one for day one: sorted distances"""
    file_content = readin_files(input_file, input_path)
    list_one, list_two = convert_list_to_numbered_list(file_content)
    list_one.sort()
    list_two.sort()
    list_diffs: list = []
    for counter, num_one in enumerate(list_one):
        list_diffs.append(abs(num_one - list_two[counter]))
    return sum(list_diffs)


def day_one_part_two(input_file, input_path: Path = Path.cwd()):
    """doing sliding window differentiation"""
    file_content = readin_files(input_file, input_path)
    list_one, list_two = convert_list_to_numbered_list(file_content)
    occourence_dict = convert_list_to_occourence_dict(list_two)
    sim_scores: list = []
    for num in list_one:
        sim_scores.append(num*occourence_dict.get(num, 0))
    return sum(sim_scores)

if __name__ == "__main__":
    my_input_path = Path.cwd() / 'assets'
    first_diff = day_one_part_one('input.txt', my_input_path)
    print(first_diff)
    print(day_one_part_two('input.txt', my_input_path))
