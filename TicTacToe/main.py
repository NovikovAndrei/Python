FIRST_PLAYER_SYMBOL = "X"
SECOND_PLAYER_SYMBOL = "0"
SIZE = 3
EMPTY_CELL = "empty"

def main():
    field = init_field(SIZE)
    print_field(field) # рисуем поле

    while True: # цикл продолжается пока не определен победитель
        player_step(field, FIRST_PLAYER_SYMBOL) # ходит первый игрок
        if is_win(field): # проверяем есть ли победитель
            print("победил игрок №1 (X)")
            break
        print_field(field) # рисуем поле после каждого хода
        if not has_empty_cell(field): # проверяем остались ли свободные ячейки
            print("Ничья")
            break

        enemy_step(field, SECOND_PLAYER_SYMBOL)
        if is_win(field):
            print("Победил игрок №2 (0)")
            break
        print_field(field)
        if not has_empty_cell(field):
            print("Ничья")
            break


def init_field(SIZE):
    """Инициализируем поле"""
    field = [[EMPTY_CELL] * SIZE for _ in range(SIZE)]
    return field

def print_field(field):
    """Рисуем поле"""
    field = [[EMPTY_CELL] * SIZE for _ in range(SIZE)]
    for line in field:
        print("| ", end="")
        for cell in line:
            print(f"{get_char(cell)} |", end=" ")
        print("")

def player_step(field, player_symbol):
    """Ход игрока №1"""
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
            print("Солбец введен некорректно. Попробуйте еще раз.")
            continue
        if not 1 <= y <= SIZE:
            print("Координата вне рамок поля. Попробуйте еще раз.")
            continue
        current_row = field[x - 1]
        current_cell = current_row[y - 1]
        if current_cell != EMPTY_CELL:
            print("Координата занята")
            continue
        cell_number = (x,y)
        return cell_number
        break

def enemy_step(field, player_symbol):
    """Ход игрока №2"""
    player_step(field,player_symbol)

def has_empty_cell(field):
    """Проверка есть ли еще пустые ячейки"""
    for row in field:
        for cell in row:
            if cell is EMPTY_CELL:
                return True
    return False

def get_char (val):
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
    current_row = field[x - 1]
    current_cell_number = current_row[y - 1]
    return current_cell_number

def is_win(field):
    """есть ли внутри поля выйгрышная комбинация"""
    win_combination = [
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)]
    ]

# Не понимаю, как дописать функцию проверки выигрыша

    if cell_1 == cell_2 == cell_3 != EMPTY_CELL:
        return True
    else:
        return False


