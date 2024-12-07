from pathlib import Path
from utils.file import readin_files


def convert_list_to_level_list(file_content: list) -> list[list[int]]:
    """file content is separated by spaces"""
    list_list: list[list[int]] = []
    for line in file_content:
        numbers = line.split(" ")
        cur_in_list = [int(val) for val in numbers]
        list_list.append(cur_in_list)

    return list_list


def check_levels(levels: list[int]) -> (bool, int):
    if levels[0] < levels[1]:
        is_increasing: bool = True
    elif levels[0] == levels[1]:
        return False, 0
    else:
        is_increasing: bool = False

    for counter, num in enumerate(levels):
        if counter + 1 == len(levels):
            break
        next_val = levels[counter + 1]
        if is_increasing:
            if num > next_val:
                return False, counter + 1
        else:
            if num < next_val:
                return False, counter + 1
        diff = abs(num - next_val)
        if diff < 1 or diff > 3:
            return False, counter + 1

    return True, len(levels)


def check_levels_two(levels: list[int]) -> (bool, list[int]):
    # get diff
    list_diff = [levels[counter + 1] - x for counter, x in enumerate(levels) if
                 counter + 1 < len(levels)]
    is_all_in_range: list[bool] = [abs(x) >= 1 and abs(x) <= 3 for x in list_diff]
    is_all_increasing: list[bool] = [x > 0 for x in list_diff]
    is_all_decreasing: list[bool] = [x < 0 for x in list_diff]
    if not all(is_all_in_range):
        return False, [counter for counter, x in enumerate(is_all_in_range) if not x]
    if all(is_all_decreasing):
        return True, len(levels)
    if all(is_all_increasing):
        return True, len(levels)
    check_inc = [counter for counter, x in enumerate(is_all_increasing) if x]
    check_dec = [counter for counter, x in enumerate(is_all_decreasing) if x]
    if len(check_dec) < len(check_inc):
        return False, check_dec
    return False, check_inc


def day_two_part_one(input_file: str, input_path: Path) -> int:
    """solving puzzle one for day one: sorted distances"""
    file_content = readin_files(input_file, input_path)
    list_of_levels = convert_list_to_level_list(file_content)
    safe_counter = 0
    for levels in list_of_levels:
        # check if list is increasing or degreasing
        is_safe, _ = check_levels(levels)
        if is_safe:
            safe_counter += 1

    return safe_counter


def day_two_part_two_version_one(input_file, input_path: Path = Path.cwd()) -> int:
    """doing sliding window differentiation"""
    file_content = readin_files(input_file, input_path)
    list_of_levels = convert_list_to_level_list(file_content)
    safe_counter = 0
    for levels in list_of_levels:
        is_safe, pos = check_levels(levels)

        if is_safe:
            safe_counter += 1
        else:
            new_levels = [x for count, x in enumerate(levels) if count != pos]
            is_now_safe, _ = check_levels_two(new_levels)
            if is_now_safe:
                safe_counter += 1

    return safe_counter


def day_two_part_two(input_file, input_path: Path = Path.cwd()) -> int:
    """doing sliding window differentiation"""
    file_content = readin_files(input_file, input_path)
    list_of_levels = convert_list_to_level_list(file_content)
    safe_counter = 0
    for levels in list_of_levels:
        if len(levels)==1:
            print("what")

        is_safe, _ = check_levels_two(levels)

        if is_safe:
            safe_counter += 1
        else:
            differences = [levels[counter + 1] - x for counter, x in enumerate(levels) if
                           counter + 1 < len(levels)]
            is_all_increasing = [x > 0 for x in differences]
            is_all_decreasing = [x < 0 for x in differences]
            all_ranges = [abs(x) > 0 and abs(x) < 4 for x in differences]

            which_position_inc = [counter for counter, x in enumerate(differences) if
                              not is_all_increasing[counter]]
            which_position_dec = [counter for counter, x in enumerate(differences) if
                              not is_all_decreasing[counter]]

            if len(which_position_inc) < len(which_position_dec):
                which_position = which_position_inc
            else:
                which_position = which_position_dec

            if len(which_position) == 0:
                which_position = [counter for counter, x in enumerate(differences) if not(all_ranges[counter])]

            if len(which_position) == 1:
                to_remove = which_position[0] +1
                to_remove_alt = which_position[0]
                new_levels = [x for counter, x in enumerate(levels) if counter != to_remove]
                new_levels_alt = [x for counter, x in enumerate(levels) if counter != to_remove_alt]
                is_safe, _ = check_levels_two(new_levels)
                is_safe_alt, _ = check_levels_two(new_levels_alt)
                if is_safe or is_safe_alt:
                    safe_counter += 1



    return safe_counter


if __name__ == "__main__":
    my_input_path = Path.cwd() / 'assets'
    print(day_two_part_one('input.txt', my_input_path))
    print(day_two_part_two_version_one("input.txt", my_input_path))
    print(day_two_part_two('input.txt', my_input_path))
