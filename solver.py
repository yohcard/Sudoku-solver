import inquirer
import os

def get_sudoku_data(grid):
    sudoku_data = []
    for row in grid:
        for cell in row:
            if cell is not None:
                sudoku_data.append(cell)
    return sudoku_data

def extract_sudoku_values(grid, size):
    values = []
    for y in range(1, size * 2, 2):
        row = []
        for x in range(1, size * 2, 2):
            row.append(grid[y][x])
        values.append(row)
    return values

def write_values_to_grid(grid, solved_values, size):
    for y in range(size):
        for x in range(size):
            grid[1 + y * 2][1 + x * 2] = solved_values[y][x]

def is_valid(board, row, col, num, size):
    box_size = int(size ** 0.5)
    num = str(num)

    for i in range(size):
        if str(board[row][i]) == num or str(board[i][col]) == num:
            return False

    start_row = row - row % box_size
    start_col = col - col % box_size
    for i in range(box_size):
        for j in range(box_size):
            if str(board[start_row + i][start_col + j]) == num:
                return False

    return True

def solve_sudoku_board(board, size):
    for row in range(size):
        for col in range(size):
            if board[row][col] == 'X' or board[row][col] == 'x':
                for num in range(1, size + 1):
                    if is_valid(board, row, col, num, size):
                        board[row][col] = str(num)
                        if solve_sudoku_board(board, size):
                            return True
                        board[row][col] = 'X'
                return False
    return True

def do_sudoku(grid, size):
    board = extract_sudoku_values(grid, size)
    if solve_sudoku_board(board, size):
        write_values_to_grid(grid, board, size)
    else:
        print("Ce sudoku est impossible à résoudre.")
        exit(1)

def generate_grid_sudoku(size):
    grid_size = size * 2 + 1  
    grid = []

    for y in range(grid_size):
        row = []
        for x in range(grid_size):
            if y % 2 == 0 and x % 2 == 0:
                print("█", end="")  # Wall
                row.append(None)
            elif y % 2 != 0 and x % 2 != 0:
                print(" ", end="")  
                row.append(None)
            else:
                print("█", end="")  
                row.append(None)
        grid.append(row)
        print()
    
    return grid

def display_grid(grid, size):
    grid_size = size * 2 + 1
    for y in range(grid_size):
        for x in range(grid_size):
            if y % 2 == 0 and x % 2 == 0:
                print("█", end="")
            elif y % 2 != 0 and x % 2 != 0:
                value = grid[y][x]
                if value is None:
                    print(" ", end="")
                else:
                    print(value, end="")
            else:
                print("█", end="")
        print()

def fill_sudoku(grid, size):
    grid_size = size * 2 + 1
    for y in range(1, grid_size, 2): 
        for x in range(1, grid_size, 2):
            while True:
                try:
                    os.system('clear' if os.name != 'nt' else 'cls')
                    display_grid(grid, size)
                    num = input(f"Entrez un chiffre pour la case ({y//2}, {x//2}) ou X si vous ne connaissez pas la réponse: ")
                    if num.isdigit() and 1 <= int(num) <= size:
                        grid[y][x] = int(num)
                        break
                    elif num.upper() == "X":
                        grid[y][x] = "X"
                        break
                    else:
                        print(f"Entrez un chiffre valide entre 1 et {size}, ou X.")
                except ValueError:
                    print("Veuillez entrer un chiffre valide.")

def main():
    print("Sudoku solver")

    questions = [
        inquirer.List('size',
                      message="Quelle est la taille de votre sudoku ?",
                      choices=['4x4', '9x9', '16x16'],  # Use valid Sudoku sizes
                      ),
    ]

    answers = inquirer.prompt(questions)

    size_map = {
        '4x4': 4,
        '9x9': 9,
        '16x16': 16
    }

    size = size_map.get(answers['size'])

    if size:
        print("Remplissez votre sudoku")
        grid = generate_grid_sudoku(size)
        fill_sudoku(grid, size)
        os.system('clear' if os.name != 'nt' else 'cls')
        do_sudoku(grid, size)
        print("Voici la solution :")
        display_grid(grid, size)
    else:
        print("Taille invalide")
        exit(1)

if __name__ == "__main__":
    main()
