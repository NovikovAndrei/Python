def get_char (val):
    """
    Функция определяет значение в поле после хода игрока
    """
    if val == 1:
        return "X"
    elif val == 2:
        return "O"
    return " "

def draw_field(field:list) -> None:
    """
    Функция рисует в консоль состояние поля
    """
    for line in field:
        for cell in line:
            get_char(cell)
        print(line)


def who_win(field) -> (int,int):
    """
    Функция определяет, кто выиграл в игре
    """
    if a == 1:
        if b == 0:
            print("Ничья")
        elif b == 1:
            print("Победил игрок №1 (X)")
        elif b == 2:
            print("Победил игрок №2 (O)")
    else:
        pass



field = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]



draw_field(field)