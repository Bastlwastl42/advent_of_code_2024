import unittest
import day_fourteen.day_14 as today
from pathlib import Path

class TestDayFourteen(unittest.TestCase):
    """Testing from given wire_input"""
    def setUp(self) -> None:
        self.test_input_folder = Path.cwd() / 'assets'
        self.test_input_file = 'test_input.txt'

    def test_day_fourteen_part_one(self):
        val = today.part_one(self.test_input_file, self.test_input_folder, (11, 7))
        self.assertEqual(12, val)
