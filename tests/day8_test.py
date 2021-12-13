from day8 import main
import unittest

class Test_Day8Part1(unittest.TestCase):
    def test_example_with_loading(self):
        all_patterns, all_digits = main.load_data("day8/test_input.txt")
        result = 26
        self.assertEqual(main.count_simple_digits(all_digits), result)

    def test_final_answer_part1(self):
        all_patterns, all_digits = main.load_data("day8/input.txt")
        result = 409
        self.assertEqual(main.count_simple_digits(all_digits), result)


class Test_Day8Part2(unittest.TestCase):
    def test_example_with_loading(self):
        all_patterns, all_digits = main.load_data("day8/test_input.txt")
        result = 61229
        self.assertEqual(main.solve_electric_problem(all_patterns, all_digits), result)

    def test_final_answer_part2(self):
        all_patterns, all_digits = main.load_data("day8/input.txt")
        result = 1024649
        self.assertEqual(main.solve_electric_problem(all_patterns, all_digits), result)
