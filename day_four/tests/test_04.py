import unittest
import day_four.day_04 as today
from pathlib import Path

class TestDayFour(unittest.TestCase):
    """Testing from given wire_input"""
    def setUp(self) -> None:
        self.test_input_folder = Path.cwd() / 'assets'
        self.test_input_file = 'test_input.txt'

    def test_day_four_part_one(self):
        val = today.day_four_part_one(self.test_input_file, self.test_input_folder)
        self.assertEqual(18, val)

    def test_day_four_part_two(self):
        val = today.day_four_part_two(self.test_input_file, self.test_input_folder)
        self.assertEqual(9, val)
