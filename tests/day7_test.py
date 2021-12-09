from day7 import main
import unittest

class Test_Day7Part1(unittest.TestCase):
    def test_example_with_loading(self):
        data = main.load_data("day7/test_input.txt")
        result = 37
        self.assertEqual(main.optimize_crab_fuel(data), result)

    def test_final_answer_part1(self):
        data = main.load_data("day7/input.txt")
        result = 344138
        self.assertEqual(main.optimize_crab_fuel(data), result)


class Test_Day7Part2(unittest.TestCase):
    def test_example_with_loading(self):
        data = main.load_data("day7/test_input.txt")
        result = 168
        self.assertEqual(main.optimize_crab_fuel_incremental(data), result)

    def test_final_answer_part2(self):
        data = main.load_data("day7/input.txt")
        result = 94862124
        self.assertEqual(main.optimize_crab_fuel_incremental(data), result)
