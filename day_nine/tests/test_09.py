import unittest
import day_nine.day_09 as today
from pathlib import Path

class TestDayNine(unittest.TestCase):
    """Testing from given wire_input"""
    def setUp(self) -> None:
        self.test_input_folder = Path.cwd() / 'assets'
        self.test_input_file = 'test_input.txt'

    def test_day_eight_part_one(self):
        val = today.part_one(self.test_input_file, self.test_input_folder)
        self.assertEqual(1928, val)

    def test_day_eight_part_two(self):
        val = today.part_two(self.test_input_file, self.test_input_folder)
        self.assertEqual(2858, val)
