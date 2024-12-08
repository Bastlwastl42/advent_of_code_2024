from pathlib import Path
from utils.file import readin_files


def get_rules_and_page_orders(file_content: list[str]) -> (list, list):
    rules_list: [(int, int)] = []
    book_list: list[list[int]] = []
    for counter, line in enumerate(file_content):
        if line == '\n':
            break
        act_rule = line.split('|')
        rules_list.append((int(act_rule[0]), int(act_rule[1])))

    for line in file_content[counter + 1:]:
        page_numbers = line.split(',')
        act_list = [int(x) for x in page_numbers]
        book_list.append(act_list)

    return rules_list, book_list


def part_one(input_file: str, input_path: Path) -> (int, list):
    """solving puzzle one for day one: sorted distances"""
    file_content = readin_files(input_file, input_path)
    rules_list, book_list = get_rules_and_page_orders(file_content)
    total_result = 0
    valued_books: list[list[int]] = []
    for book in book_list:
        book_valid = check_book(book, rules_list)
        if book_valid:
            mid_point = int(len(book) / 2)
            total_result += book[mid_point]
        else:
            valued_books.append(book)

    return total_result, valued_books


def check_book(book: list[int], rules_list) -> bool:
    book_valid = True
    for rule in rules_list:
        # both pages of the rule must be in the book
        if rule[0] in book and rule[1] in book:
            [pos_first] = [counter for counter, x in enumerate(book) if x == rule[0]]
            [pos_second] = [counter for counter, x in enumerate(book) if x == rule[1]]
            if pos_second < pos_first:
                return False
    return True


def swap_first_error(book: list[int], rules_list) -> bool:
    to_ret = [x for x in book]
    for rule in rules_list:
        if rule[0] in book and rule[1] in book:
            [pos_first] = [counter for counter, x in enumerate(book) if x == rule[0]]
            [pos_second] = [counter for counter, x in enumerate(book) if x == rule[1]]
            if pos_second < pos_first:
                to_ret[pos_first] = book[pos_second]
                to_ret[pos_second] = book[pos_first]
                return to_ret


def part_two(input_file, input_path: Path = Path.cwd()) -> int:
    """doing sliding window differentiation
    NOT DONE YET
    """
    _, valued_books = part_one(input_file, input_path)
    rules_list, _ = get_rules_and_page_orders(readin_files(input_file, input_path))
    total_results = 0
    for book in valued_books:
        cur_book = swap_first_error(book, rules_list)
        while not check_book(cur_book, rules_list):
            cur_book = swap_first_error(cur_book, rules_list)

        mid_poin = int(len(cur_book) / 2)
        total_results += cur_book[mid_poin]

    return total_results


if __name__ == "__main__":
    my_input_path = Path.cwd() / 'assets'
    printout_part_one, _ = part_one('input.txt', my_input_path)
    print(printout_part_one)
    print(part_two('input.txt', my_input_path))
