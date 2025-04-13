from unittest import TestCase
from sudoku import solve_sudoku


class TestSudoku(TestCase):

    def test_valid_sudoku(self):
        input_board = [
            5, 3, 0, 0, 7, 0, 0, 0, 0,
            6, 0, 0, 1, 9, 5, 0, 0, 0,
            0, 9, 8, 0, 0, 0, 0, 6, 0,
            8, 0, 0, 0, 6, 0, 0, 0, 3,
            4, 0, 0, 8, 0, 3, 0, 0, 1,
            7, 0, 0, 0, 2, 0, 0, 0, 6,
            0, 6, 0, 0, 0, 0, 2, 8, 0,
            0, 0, 0, 4, 1, 9, 0, 0, 5,
            0, 0, 0, 0, 8, 0, 0, 7, 9
        ]
        solution = solve_sudoku(input_board)
        self.assertIsNotNone(solution)
        self.assertEqual(len(solution), 81)

    def test_unsolvable_sudoku(self):
        # Example of a board with an obvious mistake (unsolvable)
        input_board = [
            5, 3, 0, 0, 7, 0, 0, 0, 0,
            6, 0, 0, 1, 9, 5, 0, 0, 0,
            0, 9, 8, 0, 0, 0, 0, 6, 0,
            8, 0, 0, 0, 6, 0, 0, 0, 3,
            4, 0, 0, 8, 0, 3, 0, 0, 1,
            7, 0, 0, 0, 2, 0, 0, 0, 6,
            0, 6, 0, 0, 0, 0, 2, 8, 0,
            0, 0, 0, 4, 1, 9, 0, 0, 5,
            0, 0, 0, 0, 8, 0, 0, 7, 9
        ]
        input_board[0] = 3
        solution = solve_sudoku(input_board)
        self.assertIsNone(solution)

    def test_empty_sudoku(self):
        # Test an empty Sudoku puzzle (all zeros)
        input_board = [0] * 81
        solution = solve_sudoku(input_board)
        self.assertIsNotNone(solution)
        self.assertEqual(len(solution), 81)

    def test_partially_filled_sudoku(self):
        # Test a Sudoku puzzle with some cells filled
        input_board = [
            5, 0, 0, 0, 0, 0, 4, 2, 7,
            3, 0, 2, 6, 0, 0, 0, 1, 5,
            1, 0, 0, 2, 0, 0, 6, 8, 0,
            0, 0, 0, 3, 0, 5, 8, 0, 0,
            0, 5, 1, 7, 2, 6, 0, 4, 0,
            0, 7, 3, 8, 9, 0, 0, 0, 0,
            6, 0, 0, 4, 0, 9, 0, 3, 2,
            7, 3, 0, 1, 0, 0, 0, 0, 0,
            2, 1, 9, 0, 0, 0, 7, 0, 0
        ]
        solution = solve_sudoku(input_board)
        self.assertIsNotNone(solution)
        self.assertEqual(len(solution), 81)

    def test_invalid_input_non_list(self):
        # Test non-list input returns None
        solution = solve_sudoku("Not a list")
        self.assertIsNone(solution)

    def test_invalid_input_incorrect_length(self):
        # Test input list != 81 elements returns None (incorrect length)
        input_board = [0] * 80
        solution = solve_sudoku(input_board)
        self.assertIsNone(solution)
