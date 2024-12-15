from pathlib import Path
from utils.file import readin_files
from functools import cache


def evolve(currentNumber: str) -> list:
    if currentNumber == '0':
        return ['1']
    if len(currentNumber) % 2 == 0:
        # do the split
        half = int(len(currentNumber) / 2)
        return [str(int(currentNumber[0:half])), str(int(currentNumber[half:]))]
    return [str(int(currentNumber) * 2024)]


def part_one(input_file: str, input_path: Path, iterations: int = 25) -> int:
    file_content = readin_files(input_file, input_path)
    lineOfStones = file_content[0].strip().split(' ')
    for count in range(iterations):
        if count % 5 == 0:
            print(count, end='')
        else:
            print('.', end='')

        newLineOfStones = []
        for oldStone in lineOfStones:
            if oldStone == '':
                continue
            newLineOfStones.extend(evolve(oldStone))
        lineOfStones = newLineOfStones

    return len(lineOfStones)


def countDigits(number):
    '''Count the digits of num in base 10'''
    total = 0
    while number > 0:
        total += 1
        number = number // 10
    return total


MAX_DEPTH = 75


@cache
def indepth(stone: int, depth=0):
    while depth < MAX_DEPTH:
        if stone == 0:
            stone = 1
            depth += 1
            continue

        digits = countDigits(stone)
        if digits % 2 == 0:
            mask = 10 ** (digits // 2)
            left = stone // mask
            right = stone % mask

            return indepth(left, depth + 1) + indepth(right, depth + 1)

        stone *= 2024
        depth += 1

    return 1


def part_two(input_file, input_path: Path = Path.cwd()) -> int:
    file_content = readin_files(input_file, input_path)
    lineOfStones = file_content[0].strip().split(' ')

    return sum(indepth(int(stone)) for stone in lineOfStones)


if __name__ == "__main__":
    my_input_path = Path.cwd() / 'assets'
    print(part_one('input.txt', my_input_path))
    print(part_two('input.txt', my_input_path))
