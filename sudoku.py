def solve_sudoku(input_board):
    # Validate input type
    if not isinstance(input_board, list):
        return None

    # Validate input length
    if len(input_board) != 81:
        return None
    
    # Initialise the grid from the input_board
    grid = [0] * 81
    given = [False] * 81
    box = []
    row = []
    column = []

    # Copy input_board values to grid and mark given cells
    for i in range(len(input_board)):
        if input_board[i] != 0:
            grid[i] = input_board[i]
            given[i] = True

    # Initialise box, row, and column references
    def initiate():
        box.append([0, 1, 2, 9, 10, 11, 18, 19, 20])
        box.append([3, 4, 5, 12, 13, 14, 21, 22, 23])
        box.append([6, 7, 8, 15, 16, 17, 24, 25, 26])
        box.append([27, 28, 29, 36, 37, 38, 45, 46, 47])
        box.append([30, 31, 32, 39, 40, 41, 48, 49, 50])
        box.append([33, 34, 35, 42, 43, 44, 51, 52, 53])
        box.append([54, 55, 56, 63, 64, 65, 72, 73, 74])
        box.append([57, 58, 59, 66, 67, 68, 75, 76, 77])
        box.append([60, 61, 62, 69, 70, 71, 78, 79, 80])
        for i in range(0, 81, 9):
            row.append(list(range(i, i + 9)))
        for i in range(9):
            column.append(list(range(i, 80 + i, 9)))

    # Check if number is valid at position
    def valid(n, pos):
        current_row = pos // 9
        current_col = pos % 9
        current_box = (current_row // 3) * 3 + (current_col // 3)

        for i in row[current_row]:
            if grid[i] == n:
                return False
        for i in column[current_col]:
            if grid[i] == n:
                return False
        for i in box[current_box]:
            if grid[i] == n:
                return False
        return True

    # Check if the initial board is valid
    def is_valid_board():
        for pos in range(81):
            if grid[pos] != 0:  # If cell has a value
                n = grid[pos]
                # Temporarily set to 0 to check against other cells
                grid[pos] = 0
                if not valid(n, pos):
                    # Restore value and return False
                    grid[pos] = n
                    return False
                # Restore value and continue checking
                grid[pos] = n
        return True

    # Solve the sudoku
    def solve():
        i = 0
        proceed = 1
        max_iterations = 1000000  # Add max number of iterations to detect unsolvable puzzles
        iteration_count = 0

        while i < 81 and i >= 0 and iteration_count < max_iterations:
            iteration_count += 1
            if given[i]:
                if proceed:
                    i += 1
                else:
                    i -= 1
            else:
                n = grid[i]
                prev = grid[i]
                found_valid = False

                while n < 9:
                    n += 1
                    if valid(n, i):
                        grid[i] = n
                        proceed = 1
                        found_valid = True
                        break

                if not found_valid:
                    grid[i] = 0
                    proceed = 0

                if proceed:
                    i += 1
                else:
                    i -= 1

        # Check if we solved the puzzle or failed
        if i < 0 or iteration_count >= max_iterations:
            return False  # Puzzle is unsolvable
        return True  # Puzzle solved successfully

    # Run the solver
    initiate()

    # Check if the initial board is valid
    if not is_valid_board():
        return None  # Invalid initial board

    # Try to solve
    if not solve():
        return None  # Unsolvable puzzle

    # Return the completed board
    return grid


# test the input
input_board = [5, 3, 0, 0, 7, 0, 0, 0, 0,
               6, 0, 0, 1, 9, 5, 0, 0, 0,
               0, 9, 8, 0, 0, 0, 0, 6, 0,
               8, 0, 0, 0, 6, 0, 0, 0, 3,
               4, 0, 0, 8, 0, 3, 0, 0, 1,
               7, 0, 0, 0, 2, 0, 0, 0, 6,
               0, 6, 0, 0, 0, 0, 2, 8, 0,
               0, 0, 0, 4, 1, 9, 0, 0, 5,
               0, 0, 0, 0, 8, 0, 0, 7, 9]

solution = solve_sudoku(input_board)
if solution:
    # Print the solution in a 9x9 grid
    for i in range(9):
        print(solution[i * 9:i * 9 + 9])
else:
    print("No solution exists")
