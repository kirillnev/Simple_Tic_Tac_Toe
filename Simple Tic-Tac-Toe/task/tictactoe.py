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
            string += matrix[i][j] + ' '
        string += "|"
    string += "\n---------"
    return string


def string_to_matrix(string):
    matrix = []
    for i in range(3):
        matrix.append([])
        for j in range(3):
            matrix[i].append(string[i * 3 + j])
    return matrix


def is_matrix_right(matrix):
    count_x, count_o, count_empty = 0, 0, 0
    for i in range(3):
        for j in range(3):
            count_x += 1 if matrix[i][j] == SYMBOL_X else 0
            count_o += 1 if matrix[i][j] == SYMBOL_O else 0
            count_empty += 1 if matrix[i][j] == SYMBOL_EMPTY else 0
    return abs(count_x - count_o) <= 1 and count_x + count_o + count_empty == 9


def check_col(matrix, col_number):
    count = 0
    winner_symbol = matrix[0][col_number]
    if winner_symbol != SYMBOL_EMPTY:
        for i in range(3):
            count += 1 if matrix[i][col_number] == winner_symbol else 0
        return winner_symbol if count == 3 else SYMBOL_EMPTY
    else:
        return SYMBOL_EMPTY


def check_row(matrix, row_number):
    count = 0
    winner_symbol = matrix[row_number][0]
    if winner_symbol != SYMBOL_EMPTY:
        for i in range(3):
            count += 1 if matrix[row_number][i] == winner_symbol else 0
        return winner_symbol if count == 3 else SYMBOL_EMPTY
    else:
        return SYMBOL_EMPTY


def check_diagonal(matrix, diagonal_number):
    if diagonal_number == 0 and matrix[0][0] == matrix[1][1] == matrix[2][2] or \
            diagonal_number == 1 and matrix[0][2] == matrix[1][1] == matrix[2][0]:
        return matrix[1][1]
    else:
        return SYMBOL_EMPTY


def check_result(matrix):
    rows_result = [check_row(matrix, i) for i in range(3)]
    cols_result = [check_col(matrix, i) for i in range(3)]
    diagonals_result = [check_diagonal(matrix, i) for i in range(2)]
    x_wins_count = 0
    o_wins_count = 0
    empty_count = 0
    for i in range(3):
        for j in range(3):
            empty_count += 1 if matrix[i][j] == SYMBOL_EMPTY else 0
    for i in range(3):
        x_wins_count += 1 if rows_result[i] == SYMBOL_X else 0
        x_wins_count += 1 if cols_result[i] == SYMBOL_X else 0
        o_wins_count += 1 if rows_result[i] == SYMBOL_O else 0
        o_wins_count += 1 if cols_result[i] == SYMBOL_O else 0
    for i in range(2):
        x_wins_count += 1 if diagonals_result[i] == SYMBOL_X else 0
        o_wins_count += 1 if diagonals_result[i] == SYMBOL_O else 0
    if x_wins_count > 0 and o_wins_count > 0 or x_wins_count > 1 or o_wins_count > 1:
        return "Impossible"
    elif x_wins_count == 1:
        return "X wins"
    elif o_wins_count == 1:
        return "O wins"
    elif empty_count > 0:
        return "Game not finished"
    else:
        return "Draw"


if __name__ == "__main__":
    input_string = input()
    if is_input_correct(input_string):
        field = string_to_matrix(input_string)
        print(matrix_to_string(field))
        if is_matrix_right(field):
            print(check_result(field))
        else:
            print("Impossible")
    else:
        print("Incorrect input data")
