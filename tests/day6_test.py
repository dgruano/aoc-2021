from day6 import main
import unittest

class Test_Day6Part1(unittest.TestCase):
    def test_example_with_loading(self):
        data = main.load_data("day6/test_input.txt")
        result = 5934
        self.assertEqual(main.get_lanternfish_growth(data, days=80), result)

    def test_final_answer_part1(self):
        data = main.load_data("day6/input.txt")
        result = 371379
        self.assertEqual(main.get_lanternfish_growth(data, days=80), result)

    def test_final_answer_part1_opt(self):
        data = main.load_data("day6/input.txt")
        result = 371379
        self.assertEqual(main.get_lanternfish_counters(data, days=80), result)


class Test_Day6Part2(unittest.TestCase):
    def test_example_with_loading(self):
        data = main.load_data("day6/test_input.txt")
        result = 26984457539
        self.assertEqual(main.get_lanternfish_counters(data, days=256), result)

    def test_final_answer_part2_opt(self):
        data = main.load_data("day6/input.txt")
        result = 1674303997472
        self.assertEqual(main.get_lanternfish_counters(data, days=256), result)
