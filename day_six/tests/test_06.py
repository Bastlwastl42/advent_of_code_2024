import unittest
import day_six.day_06 as today
from pathlib import Path

class TestDaysix(unittest.TestCase):
    """Testing from given wire_input"""
    def setUp(self) -> None:
        self.test_input_folder = Path.cwd() / 'assets'
        self.test_input_file = 'test_input.txt'

    def test_day_six_part_one(self):
        val = today.part_one(self.test_input_file, self.test_input_folder)
        self.assertEqual(41, val)

    def test_day_six_part_two(self):
        val = today.part_two(self.test_input_file, self.test_input_folder)
        self.assertEqual(123, val)
