import unittest
from day_three.day_03 import day_three_part_one, day_three_part_two
from pathlib import Path

class TestDayTwo(unittest.TestCase):
    """Testing from given wire_input"""
    def setUp(self) -> None:
        self.test_input_folder = Path.cwd() / 'assets'
        self.test_input_file = 'test_input.txt'
        self.test_input_file_2 = 'test_input_2.txt'

    def test_day_three_part_one(self):
        val = day_three_part_one(self.test_input_file, self.test_input_folder)
        self.assertEqual(161, val)

    def test_day_three_part_two(self):
        val = day_three_part_two(self.test_input_file_2, self.test_input_folder)
        self.assertEqual(48, val)
