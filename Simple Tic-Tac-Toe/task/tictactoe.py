SYMBOL_X = 'X'
SYMBOL_O = 'O'
SYMBOL_EMPTY = '_'


def matrix_to_string(matrix):
    string = "---------"
    for i in range(3):
        string += "\n| "
        for j in range(3):
            if matrix[i][j] == 0:
                string += SYMBOL_EMPTY + ' '
            elif matrix[i][j] == 1:
                string += SYMBOL_X + ' '
            else:
                string += SYMBOL_O + ' '

        string += "|"
    string += "\n---------"
    return string


# Returns 1 or 2 if someone wins
# 0 if there are free cells
# -1 if it is a draw
def check_col(matrix, col):
    result = 1
    for i in range(3):
        result *= matrix[i][col]
    if 1 < result < 8:
        result = -1
    elif result == 8:
        result = 2
    return result


def check_row(matrix, row):
    result = 1
    for i in range(3):
        result *= matrix[row][i]
    if 1 < result < 8:
        result = -1
    elif result == 8:
        result = 2
    return result


def check_diagonal(matrix, diagonal):
    result = 1
    for i in range(3):
        result *= matrix[i][i] if diagonal == 0 else matrix[i][2 - i]
    if 1 < result < 8:
        result = -1
    elif result == 8:
        result = 2
    return result


def check_result(matrix):
    rows_result = [check_row(matrix, i) for i in range(3)]
    cols_result = [check_col(matrix, i) for i in range(3)]
    diagonals_result = [check_diagonal(matrix, i) for i in range(2)]
    result_list = rows_result + cols_result + diagonals_result

    if 1 in result_list:
        return 1
    elif 2 in result_list:
        return 2
    elif not all(result_list):
        return 0
    else:
        return -1


def print_result(result):
    if result == 1:
        print("X wins")
    elif result == 2:
        print("O wins")
    else:
        print("Draw")


def is_cell_empty(matrix, i, j):
    return matrix[i][j] == 0


def input_cell(matrix, cell_value):
    is_exit = False
    while not is_exit:
        try:
            i, j = input().split()
            i = int(i)
            j = int(j)
            if 1 <= i <= 3 and 1 <= j <= 3:
                if is_cell_empty(matrix, i - 1, j - 1):
                    is_exit = True
                    matrix[i - 1][j - 1] = cell_value
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")
        except ValueError:
            print("You should enter numbers!")


def go():
    matrix = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    print(matrix_to_string(matrix))
    result = 0
    cell_value = 1

    while result == 0:
        input_cell(matrix, cell_value)
        cell_value = 2 if cell_value == 1 else 1
        print(matrix_to_string(matrix))
        result = check_result(matrix)

    print_result(result)


if __name__ == "__main__":
    go()
