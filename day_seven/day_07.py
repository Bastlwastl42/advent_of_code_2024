from pathlib import Path
from utils.file import readin_files
from itertools import product

def split_line_to_exp_and_numbers(input_lines: list[str]) -> dict[int, list[int]]:
    ret_val: dict[int, lint[int]] = {}
    for line in input_lines:
        exp_result, rest = line.split(':')
        ret_val[int(exp_result)] = [int(x) for x in rest.strip().split(' ')]
    return ret_val


def operate(num1: int, num2: int, operator: str) -> int:
    if operator == '+':
        return num1 + num2
    if operator == "*":
        return num1 * num2


def operate_all(numbers: list[int], operators: list[str]) -> int:
    result = numbers[0]
    for counter, op in enumerate(operators):
        result = operate(result, numbers[counter + 1], op)
    return result


def all_ops_are_mul(operators) -> bool:
    return all([x == '*' for x in operators])


def get_all_operations(lenght_of_operator_list: int) -> list[str]:
    all_op_ret = []
    for operators in product('+*', repeat=lenght_of_operator_list):
        cur_op = []
        for op in operators:
            cur_op.append(op)
        all_op_ret.append(cur_op)
    return all_op_ret


def part_one(input_file: str, input_path: Path) -> int:
    """solving puzzle one for day one: sorted distances"""
    file_content = readin_files(input_file, input_path)
    result_dict = split_line_to_exp_and_numbers(file_content)
    12839601725877
    total_result = 0
    for exp_result, numbers in result_dict.items():
        all_op = get_all_operations(len(numbers) - 1)
        for operators in all_op:
            test_res = operate_all(numbers, operators)
            if test_res == exp_result:
                total_result += exp_result
                break

    return total_result


def part_two(input_file, input_path: Path = Path.cwd()) -> int:
    return 0


if __name__ == "__main__":
    my_input_path = Path.cwd() / 'assets'
    print(part_one('input.txt', my_input_path))
    print(part_two('input.txt', my_input_path))
