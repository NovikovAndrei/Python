FIRST_PLAYER_SYMBOL = "X"
SECOND_PLAYER_SYMBOL = "0"
EMPTY_CELL = " "
SIZE = int(input("Введите размер поля: "))

def main():
    field = init_field(SIZE)
    print_field(field)  # рисуем поле
    game(field, FIRST_PLAYER_SYMBOL, SIZE)  # ну или тот символ, что выберет пользователь


def game(field, player, size):
    win_combination = get_win_combinations(size)
    current_player = player
    while True:  # цикл продолжается пока не определен победитель
        point = player_step(field)  # ходит игрок
        field[point[0]][point[1]] = current_player
        print_field(field)
        if is_win(field, win_combination, size):  # проверяем есть ли победитель
            print(f"\t  Победил игрок - ({current_player})")
            print("                ⠀  ⠀⠀⠀／＞　 フ\n \
            　　　　　| 　_　 _|\n \
            　 　　　／`ミ _x 彡\n \
            　　 　 /　　　 　 |\n \
            　　　 /　 ヽ　　 ﾉ\n \
            　／￣|　　 |　|　|\n \
            　| (￣ヽ＿_ヽ_)_)\n \
            　＼二つ")
            break
        if not has_empty_cell(field):  # проверяем остались ли свободные ячейки
            print("\tНичья")
            break
        current_player = FIRST_PLAYER_SYMBOL if current_player == SECOND_PLAYER_SYMBOL else SECOND_PLAYER_SYMBOL


def init_field(size):
    """Инициализируем поле"""
    field = [[EMPTY_CELL] * size for _ in range(size)]
    return field


def print_field(field):
    """Рисуем поле"""
    sep = "- - " * SIZE
    sep_size = sep + '- '
    print(sep_size)
    for line in field:
        print("| ", end="")
        for cell in line:
            print(f"{cell} |", end=" ")
        print("")
        print(sep_size)


def player_step(field):
    """Ход игрока"""
    while True:
        try:
            x = int(input("Введите номер строки: "))
        except ValueError:
            print("Строка введена некорректно. Попробуйте еще раз.")
            continue
        if not 1 <= x <= SIZE:
            print("Координата вне рамок поля. Попробуйте еще раз.")
            continue
        try:
            y = int(input("Введите номер столбца: "))
        except ValueError:
            print("Столбец введен некорректно. Попробуйте еще раз.")
            continue
        if not 1 <= y <= SIZE:
            print("Координата вне рамок поля. Попробуйте еще раз.")
            continue
        current_row = field[x - 1]
        current_cell = current_row[y - 1]
        if current_cell != EMPTY_CELL:
            print("Координата занята")
            continue
        cell_number = (x - 1, y - 1)
        return cell_number


def has_empty_cell(field):
    """Проверка есть ли еще пустые ячейки"""
    for row in field:
        for cell in row:
            if cell is EMPTY_CELL:
                return True
    return False


def get_char(val):
    """
    Функция определяет значение в поле после хода игрока
    """
    # не понимаю как менять пустую клетку в поле на X или 0
    if val == 1:
        return "X"
    elif val == 2:
        return "O"
    return EMPTY_CELL


def get_cell(field, cell_number):
    """Получает ячейку из координат"""
    return field[cell_number[0] - 1][cell_number[1] - 1]


def get_win_combinations(size):  # создаёт индексы выгрышных комбинаций
    diagonal1 = []
    diagonal2 = []
    rows = []
    cols = []
    for i in range(size):
        tmp_row = []
        tmp_col = []
        for j in range(size):
            tmp_row.append((i, j))
            tmp_col.append((j, i))
        rows.append(tmp_row)
        cols.append(tmp_col)
        diagonal1.append((i, i))
        diagonal2.append((i, size - 1 - i))

    return rows + cols + [diagonal1] + [diagonal2]


def is_win(field, win_combination, size):
    """есть ли внутри поля выйгрышная комбинация"""
    count = 1
    for comb in win_combination:
        current_symbol = field[comb[0][0]][comb[0][1]]
        for i_row, i_col in comb[1:]:
            if field[i_row][i_col] == current_symbol:
                count += 1
                if count == size and current_symbol != EMPTY_CELL:
                    return True
            else:
                count = 1
    return False


if __name__ == "__main__":
    main()
