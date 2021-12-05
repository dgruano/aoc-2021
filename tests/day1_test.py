from day1 import main
import unittest

class Test_Day1Part1(unittest.TestCase):
    def test_always_increase(self):
        data = list(range(100))
        result = 99
        self.assertEqual(main.count_larger_than_previous(data), result)
    
    def test_always_decrease(self):
        data = list(range(0, 100, -1))
        result = 0
        self.assertEqual(main.count_larger_than_previous(data), result)

    def test_no_data(self):
        data = []
        result = 0
        self.assertEqual(main.count_larger_than_previous(data), result)

    def test_all_equal(self):
        data = [1] * 100
        result = 0
        self.assertEqual(main.count_larger_than_previous(data), result)

    def test_example_part1(self):
        data = [199,200,208,210,200,207,240,269,260,263]
        result = 7
        self.assertEqual(main.count_larger_than_previous(data), result)

    def test_example_part1_with_loading(self):
        data = main.load_data("day1/test_input.txt")
        result = 7
        self.assertEqual(main.count_larger_than_previous(data), result)

    def test_final_answer_part1(self):
        data = main.load_data("day1/input.txt")
        result = 1532
        self.assertEqual(main.count_larger_than_previous(data), result)


class Test_Day1Part2(unittest.TestCase):
    def test_example_part2(self):
        data = [199,200,208,210,200,207,240,269,260,263]
        result = 5
        self.assertEqual(main.count_larger_than_previous_window(data, 3), result)

    def test_example_part2_opt(self):
        data = [199,200,208,210,200,207,240,269,260,263]
        result = 5
        self.assertEqual(main.count_larger_than_previous_window_opt(data, 3), result)
    
    def test_final_answer_part2(self):
        data = main.load_data("day1/input.txt")
        result = 1571
        self.assertEqual(main.count_larger_than_previous_window(data, 3), result)