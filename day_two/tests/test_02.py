import unittest
from day_two.day_02 import day_two_part_one, day_two_part_two
from pathlib import Path

class TestDayTwo(unittest.TestCase):
    """Testing from given wire_input"""
    def setUp(self) -> None:
        self.test_input_folder = Path.cwd() / 'assets'
        self.test_input_file = 'test_input.txt'

    def test_day_one_part_one(self):
        val = day_two_part_one(self.test_input_file, self.test_input_folder)
        self.assertEqual(2, val)

    def test_day_one_part_two(self):
        val = day_two_part_two(self.test_input_file, self.test_input_folder)
        self.assertEqual(4, val)
