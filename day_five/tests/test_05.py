import unittest
import day_five.day_05 as today
from pathlib import Path

class TestDayFive(unittest.TestCase):
    """Testing from given wire_input"""
    def setUp(self) -> None:
        self.test_input_folder = Path.cwd() / 'assets'
        self.test_input_file = 'test_input.txt'

    def test_day_five_part_one(self):
        val, _ = today.part_one(self.test_input_file, self.test_input_folder)
        self.assertEqual(143, val)

    def test_day_five_part_two(self):
        val = today.part_two(self.test_input_file, self.test_input_folder)
        self.assertEqual(123, val)
