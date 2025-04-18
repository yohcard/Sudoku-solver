# Sudoku Solver

This Python program is a simple Sudoku solver and generator. It allows users to fill in a Sudoku grid and solve it using a backtracking algorithm. The program supports different grid sizes (4x4, 9x9, and 16x16), and it allows you to enter values manually or leave cells marked as "X" for unknown values. Once the puzzle is filled, the program will attempt to solve it and display the solution.

## Features:
- **Sudoku Grid Generation:** Generate grids of different sizes (4x4, 9x9, 16x16) for solving.
- **Manual Input:** Fill in the Sudoku grid manually, marking unknown cells with "X".
- **Sudoku Solver:** Solve the Sudoku puzzle using a backtracking algorithm.
- **Grid Display:** Display the grid in a clear format with walls and cells separated.

## Requirements:
- Python 3.x
- `inquirer` library for interactive input prompts

## How to Use:

1. **Install Dependencies:**  
   Make sure to install the necessary dependencies by running:
   ```bash
   pip install inquirer
   ```

2. **Run the Program:**
   To run the Sudoku solver, simply execute the program:
   ```bash
   python sudoku_solver.py
   ```

3. **Follow the Prompts:**
   The program will ask you to select the size of the Sudoku puzzle (4x4, 9x9, or 16x16), then you can fill the grid by entering values for each cell. If you don't know the value, input "X" to leave it blank. Once filled, the program will solve the puzzle and show the solution.

## Functions:
- `get_sudoku_data(grid)`: Extracts all the non-empty values from the grid.
- `extract_sudoku_values(grid, size)`: Extracts the Sudoku values from the grid for solving.
- `write_values_to_grid(grid, solved_values, size)`: Writes the solved Sudoku values back into the grid.
- `is_valid(board, row, col, num, size)`: Checks if a number can be placed in a given cell based on Sudoku rules.
- `solve_sudoku_board(board, size)`: Solves the Sudoku puzzle using a backtracking algorithm.
- `do_sudoku(grid, size)`: Solves the Sudoku puzzle and updates the grid with the solution.
- `generate_grid_sudoku(size)`: Generates a Sudoku grid with the specified size.
- `display_grid(grid, size)`: Displays the Sudoku grid in a user-friendly format.
- `fill_sudoku(grid, size)`: Prompts the user to fill in the Sudoku grid manually.

## Example Output:
```
Sudoku solver
Quelle est la taille de votre sudoku ?
  - 4x4
  - 9x9
  - 16x16

Remplissez votre sudoku
[Sudoku grid display]
Entrez un chiffre pour la case (1, 1) ou X si vous ne connaissez pas la réponse: 5
[Sudoku grid display]
[...]
Voici la solution :
[Sudoku solved grid display]
```

## License:
This project is open-source.

