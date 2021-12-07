from day5 import main
import unittest

class Test_Day5Part1(unittest.TestCase):
    def test_example_with_loading(self):
        data = main.load_data("day5/test_input.txt")
        result = 5
        self.assertEqual(main.get_crossing_points(data, l=10, simple=True), result)

    def test_final_answer_part1(self):
        data = main.load_data("day5/input.txt")
        result = 5147
        self.assertEqual(main.get_crossing_points(data, simple=True), result)

class Test_Day5Part2(unittest.TestCase):
    def test_example_with_loading(self):
        data = main.load_data("day5/test_input.txt")
        result = 12
        self.assertEqual(main.get_crossing_points(data, l=10), result)

    def test_final_answer_part1(self):
        data = main.load_data("day5/input.txt")
        result = 16925
        self.assertEqual(main.get_crossing_points(data), result)