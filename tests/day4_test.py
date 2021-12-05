from day4 import main
import unittest

class Test_Day4Part1(unittest.TestCase):
    def test_example_with_loading(self):
        bingo, boards = main.load_data("day4/test_input.txt")
        result = 4512
        self.assertEqual(main.get_winner_board(bingo, boards), result)

    def test_final_answer_part1(self):
        bingo, boards = main.load_data("day4/input.txt")
        result = 39902
        self.assertEqual(main.get_winner_board(bingo, boards), result)


class Test_Day4Part2(unittest.TestCase):
    def test_example_with_loading(self):
        bingo, boards = main.load_data("day4/test_input.txt")
        result = 1924
        self.assertEqual(main.get_loser_board(bingo, boards), result)

    def test_final_answer_part1(self):
        bingo, boards = main.load_data("day4/input.txt")
        result = 26936
        self.assertEqual(main.get_loser_board(bingo, boards), result)   