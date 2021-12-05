from day3 import main
import unittest

class Test_Day3Part1(unittest.TestCase):
    def test_example_with_loading(self):
        data = main.load_data("day3/test_input.txt")
        result = 198
        self.assertEqual(main.most_common_bit(data), result)
    
    def test_example_pandas(self):
        data = main.load_data("day3/test_input.txt")
        result = 198
        self.assertEqual(main.most_common_bit_pd(data), result)
    
    def test_final_answer_part1(self):
        data = main.load_data("day3/input.txt")
        result = 4191876
        self.assertEqual(main.most_common_bit(data), result)


class Test_Day3_Part2(unittest.TestCase):
    def test_example_part2_with_loading(self):
        data = main.load_data("day3/test_input.txt")
        result = 230
        self.assertEqual(main.most_common_bit_part2(data), result)

    def test_example_part2_pandas(self):
        data = main.load_data("day3/test_input.txt")
        result = 230
        self.assertEqual(main.most_common_bit_part2_pd(data), result)

    def test_equal_number_part2_pandas(self):
        """
        Checks correct behaviour when there is the same number of 1s and 0s
        for one bit position.
        NOTE: A good testing dataset must:
            1. Not contain binary 0 as an option. This may cause the result to be 0
            by mutiplication of any number by 0, so many incorrect calculations would
            appear as correct.
            
            2. Be shuffled. This way, the selection of the most frequent bit will not
            be sistematically chosen based on the order of the occurrences. This can
            be done in the file or at runtime (I chose the former).
        """
        
        data = main.load_data("day3/custom_input1.txt")
        result = 15
        self.assertEqual(main.most_common_bit_part2_pd(data), result)

    def test_final_answer_part2(self):
        data = main.load_data("day3/input.txt")
        result = 3414905
        self.assertEqual(main.most_common_bit_part2(data), result)
    
    def test_final_answer_part2_pandas(self):
        data = main.load_data("day3/input.txt")
        result = 3414905
        self.assertEqual(main.most_common_bit_part2_pd(data), result)