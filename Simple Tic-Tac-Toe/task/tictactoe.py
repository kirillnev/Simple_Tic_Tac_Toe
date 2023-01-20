SYMBOL_X = 'X'
SYMBOL_O = 'O'
SYMBOL_EMPTY = '_'


def is_input_correct(string):
    if len(string) == 9:
        for i in range(9):
            if string[i] != SYMBOL_X and string[i] != SYMBOL_O and string[i] != SYMBOL_EMPTY:
                return False
        return True
    else:
        return False


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


def string_to_matrix(string):
    matrix = []
    for i in range(3):
        matrix.append([])
        for j in range(3):
            value = 1 if string[i * 3 + j] == SYMBOL_X else 2 if string[i * 3 + j] == SYMBOL_O else 0
            matrix[i].append(value)
    return matrix


def is_matrix_right(matrix):
    count_x, count_o, count_empty = 0, 0, 0
    for i in range(3):
        for j in range(3):
            count_x += 1 if matrix[i][j] == 1 else 0
            count_o += 1 if matrix[i][j] == 2 else 0
            count_empty += 1 if matrix[i][j] == 0 else 0
    return abs(count_x - count_o) <= 1 and count_x + count_o + count_empty == 9


def check_col(matrix, col):
    result = 1
    for i in range(3):
        result *= matrix[i][col]
    return result


def check_row(matrix, row):
    result = 1
    for i in range(3):
        result *= matrix[row][i]
    return result


def check_diagonal(matrix, diagonal):
    result = 1
    for i in range(3):
        result *= matrix[i][i] if diagonal == 0 else matrix[i][2 - i]
    return result


def check_result(matrix):
    rows_result = [check_row(matrix, i) for i in range(3)]
    cols_result = [check_col(matrix, i) for i in range(3)]
    diagonals_result = [check_diagonal(matrix, i) for i in range(2)]
    result = 0

    if 1 in rows_result and 8 in rows_result or \
        1 in cols_result and 8 in cols_result or \
        1 in diagonals_result and 8 in diagonals_result:
        raise ValueError

    if 1 in rows_result or 1 in cols_result or 1 in diagonals_result:
        result = 1
    elif 8 in rows_result or 8 in cols_result or 8 in diagonals_result:
        result = 2
    elif 0 in rows_result or 0 in cols_result or 0 in diagonals_result:
        result = 0
    else:
        result = -1

    return result


def print_result(result):
    if result == 1:
        print("X wins")
    elif result == 2:
        print("O wins")
    elif result == 0:
        print("Game is not finished")
    else:
        print("Draw")


def is_cell_empty(matrix, i, j):
    return matrix[i][j] == 0


def input_cell(matrix):
    is_exit = False
    while not is_exit:
        try:
            i, j = input().split()
            i = int(i)
            j = int(j)
            if 1 <= i <= 3 and 1 <= j <= 3:
                if is_cell_empty(matrix, i - 1, j - 1):
                    is_exit = True
                    matrix[i - 1][j - 1] = 1
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")
        except ValueError:
            print("You should enter numbers!")


def go():
    input_string = input()
    try:
        if not is_input_correct(input_string):
            raise ValueError
        matrix = string_to_matrix(input_string)
        print(matrix_to_string(matrix))
        if not is_matrix_right(matrix):
            raise ValueError

        input_cell(matrix)
        print(matrix_to_string(matrix))

    except ValueError:
        print("Impossible")


if __name__ == "__main__":
    go()
