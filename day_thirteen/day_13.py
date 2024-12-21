from pathlib import Path
from utils.file import readin_files

PRIZE_A = 3
PRIZE_B = 1
MAX_PLAYTIME = 100
PART_TWO_EXTRA = 10000000000000


# target_x = button_a_pushes*button_a_move_x + button_b_pushes*button_b_move_x
# target_y = button_a_pushes*button_a_move_y + button_b_pushes*button_b_move_y
# max_playtime >= button_a_pushes + button_b_pushes


class ClawMaschine:
    target: tuple[int, int]
    target_part_two: tuple[int, int]
    button_a_move: tuple[int, int]
    button_b_move: tuple[int, int]

    def __init__(self, lineInput: list[str]):
        # first line is button A
        _, coords = lineInput[0].split(':')
        x, y = coords.split(',')
        _, buttonAX = x.split('+')
        _, buttonAY = y.split('+')

        _, coords = lineInput[1].split(':')
        x, y = coords.split(',')
        _, buttonBX = x.split('+')
        _, buttonBY = y.split('+')

        _, prize_cords = lineInput[2].split(':')
        x, y = prize_cords.split(',')
        _, prizeX = x.split('=')
        _, prizeY = y.split('=')

        self.target = (int(prizeX), int(prizeY.strip()))
        self.button_a_move = (int(buttonAX), int(buttonAY.strip()))
        self.button_b_move = (int(buttonBX), int(buttonBY.strip()))
        self.target_part_two = (int(prizeX) + PART_TWO_EXTRA, int(prizeY.strip()) + PART_TWO_EXTRA)

    def det(self):
        return self.button_a_move[0] * self.button_b_move[1] - self.button_a_move[1] * \
               self.button_b_move[0]

    def det_1(self, partone: bool = True):
        if partone:
            return self.target[0] * self.button_b_move[1] - self.target[1] * self.button_b_move[0]
        return self.target_part_two[0] * self.button_b_move[1] - self.target_part_two[1] * \
               self.button_b_move[0]

    def det_2(self, partone: bool = True):
        if partone:
            return self.button_a_move[0] * self.target[1] - self.button_a_move[1] * self.target[0]
        return self.button_a_move[0] * self.target_part_two[1] - self.button_a_move[1] * \
               self.target_part_two[0]

    def solve(self, partone: bool = True) -> tuple[int, int]:
        if self.det() == 0:
            return 0, 0

        x_1 = self.det_1(partone) / self.det()
        x_2 = self.det_2(partone) / self.det()
        if int(x_1) != x_1 \
                or int(x_2) != x_2 \
                or x_1 < 0 or x_2 < 0:
            return 0, 0

        return int(x_1), int(x_2)

    def solve_iter(self):
        full_target = sum(self.target)
        full_a = sum(self.button_a_move)
        full_b = sum(self.button_b_move)
        for a_counter in range(MAX_PLAYTIME + 1):
            if full_target > a_counter * full_a + 100 * full_b:
                continue
            for b_counter in range(MAX_PLAYTIME + 1):
                if a_counter * full_a + b_counter * full_b == full_target:
                    return a_counter, b_counter
        return 0, 0


def part_one(input_file: str, input_path: Path, iterations: int = 25) -> int:
    file_content = readin_files(input_file, input_path)
    all_them_claws: list[ClawMaschine] = []
    current_stack = []
    for line in file_content:
        if line != "\n":
            current_stack.append(line)
            continue
        if len(current_stack) == 3:
            all_them_claws.append(ClawMaschine(current_stack))
            current_stack = []

    list_of_solutions: list[tuple[int, int]] = []
    for claw in all_them_claws:
        list_of_solutions.append(claw.solve())

    total_input = 0
    for solution in list_of_solutions:
        if solution == (0, 0):
            continue
        total_input += solution[0] * PRIZE_A + solution[1] * PRIZE_B

    return total_input


def part_two(input_file, input_path: Path = Path.cwd()) -> int:
    file_content = readin_files(input_file, input_path)
    all_them_claws: list[ClawMaschine] = []
    current_stack = []
    for line in file_content:
        if line != "\n":
            current_stack.append(line)
            continue
        if len(current_stack) == 3:
            all_them_claws.append(ClawMaschine(current_stack))
            current_stack = []

    list_of_solutions: list[tuple[int, int]] = []
    for claw in all_them_claws:
        list_of_solutions.append(claw.solve(partone=False))

    total_input = 0
    for solution in list_of_solutions:
        if solution == (0, 0):
            continue
        total_input += solution[0] * PRIZE_A + solution[1] * PRIZE_B

    return total_input

if __name__ == "__main__":
    my_input_path = Path.cwd() / 'assets'
    print(part_one('input.txt', my_input_path))
    print(part_two('input.txt', my_input_path))
