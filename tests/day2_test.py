from day2 import main
import unittest

class Test_Day2Part1(unittest.TestCase):
    def test_example_with_loading(self):
        data = main.load_data("day2/test_input.txt")
        result = 150
        self.assertEqual(main.calculate_coordinates(data), result)
    
    def test_negative_depth(self):
        # Cannot go higher than depth=0
        data = [["forward", 1], ["up", 1]]
        result = 0
        self.assertEqual(main.calculate_coordinates(data), result)

    def test_final_answer_part1(self):
        data = main.load_data("day2/input.txt")
        result = 1840243
        self.assertEqual(main.calculate_coordinates(data), result)     


class Test_Day2Part2(unittest.TestCase):
    def test_example_part2_with_loading(self):
        data = main.load_data("day2/test_input.txt")
        result = 900
        self.assertEqual(main.calculate_coordinates_part2(data), result)
    
    def test_final_answer_part2(self):
        data = main.load_data("day2/input.txt")
        result = 1727785422
        self.assertEqual(main.calculate_coordinates_part2(data), result)
        

