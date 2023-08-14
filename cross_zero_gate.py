def get_start_desk():
    """Show initial desk with numbered cells"""

    example_desk = [
        [' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' '],
        [' ', '1', ' ', '|', ' ', ' ', '2', ' ', ' ', '|', ' ', '3', ' '],
        [' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' '],
        ['-', '-', '-', '|', '-', '-', '-', '-', '-', '|', '-', '-', '-'],
        [' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' '],
        [' ', '4', ' ', '|', ' ', ' ', '5', ' ', ' ', '|', ' ', '6', ' '],
        [' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' '],
        ['-', '-', '-', '|', '-', '-', '-', '-', '-', '|', '-', '-', '-'],
        [' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' '],
        [' ', '7', ' ', '|', ' ', ' ', '8', ' ', ' ', '|', ' ', '9', ' '],
        [' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' '],
    ]
    return example_desk

def win(desk, sign):
    """Check if sign is win"""

    cells_dict = {
        '1': desk[1][1], '2': desk[1][6], '3': desk[1][11],
        '4': desk[5][1], '5': desk[5][6], '6': desk[5][11],
        '7': desk[9][1], '8': desk[9][6], '9': desk[9][11]
    }

    sign_sells = [cell_number for cell_number, cell_value in cells_dict.items() if cell_value == sign]
    if '1' in sign_sells and '2' in sign_sells and '3' in sign_sells:
        return True
    elif '4' in sign_sells and '5' in sign_sells and '6' in sign_sells:
        return True
    elif '7' in sign_sells and '8' in sign_sells and '9' in sign_sells:
        return True
    elif '1' in sign_sells and '4' in sign_sells and '7' in sign_sells:
        return True
    elif '8' in sign_sells and '5' in sign_sells and '2' in sign_sells:
        return True
    elif '9' in sign_sells and '6' in sign_sells and '3' in sign_sells:
        return True
    elif '7' in sign_sells and '5' in sign_sells and '3' in sign_sells:
        return True
    elif '1' in sign_sells and '5' in sign_sells and '9' in sign_sells:
        return True
    else:
        return False


def show_desk(game_desk):
    """Show current desk state"""

    for line in game_desk:
        string_line = ''
        for elm in line:
            string_line += elm
        print(string_line)


def get_free_cells(desk):
    """Return free desk cells"""
    cells_dict = {
        '1': desk[1][1], '2': desk[1][6], '3': desk[1][11],
        '4': desk[5][1], '5': desk[5][6], '6': desk[5][11],
        '7': desk[9][1], '8': desk[9][6], '9': desk[9][11]
    }
    free_cells = []
    for cell_number, cell_value in cells_dict.items():
        if cell_value == ' ':
            free_cells.append(cell_number)

    return free_cells


def set_step(desk, number, sign):
    """Set game sign"""

    match number:
        case '1':
            desk[1][1] = sign
        case '2':
            desk[1][6] = sign
        case '3':
            desk[1][11] = sign
        case '4':
            desk[5][1] = sign
        case '5':
            desk[5][6] = sign
        case '6':
            desk[5][11] = sign
        case '7':
            desk[9][1] = sign
        case '8':
            desk[9][6] = sign
        case '9':
            desk[9][11] = sign

    return desk


def loop():
    """Game"""

    answer = ''
    while answer not in ('x', 'X', 'o', 'O', '0'):
        answer = input("Так кем вы хотите играть - x или o?")
    if answer in ['x', 'X']:
        first_player_sign, second_player_sign = 'x', 'o'
    else:
        first_player_sign, second_player_sign = 'o', 'x'

    game_desk = [
        [' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' '],
        [' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' '],
        [' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' '],
        ['-', '-', '-', '|', '-', '-', '-', '-', '-', '|', '-', '-', '-'],
        [' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' '],
        [' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' '],
        [' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' '],
        ['-', '-', '-', '|', '-', '-', '-', '-', '-', '|', '-', '-', '-'],
        [' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' '],
        [' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' '],
        [' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' '],
    ]
    show_desk(game_desk)
    first_player_step = True

    while True:
        step = 0
        sign = first_player_sign if first_player_step else second_player_sign
        player = 'Игрок 1' if first_player_step else 'Игрок 2'
        while step not in get_free_cells(game_desk):
            step = input(f'{player} ({sign}): Выберите следующую клетку: (1-9)')
        game_desk = set_step(game_desk, step, sign)
        show_desk(game_desk)
        if win(game_desk, sign):
            print(f"{player} ({sign}) выиграл!")
            break
        if not get_free_cells(game_desk):
            print('Ничья - свободных клеток нет')
            break
        first_player_step = not first_player_step

def game():
    """Loop"""

    print("=" * 40)
    print("Добро пожаловать в крестики-нолики!")
    print("Сперва выберите свой знак - x или o!")
    print("Затем по очереди жмите цифры!")
    print("Цифра = клетка на поле, куда вы поставите знак!")
    print("=" * 40)

    example = get_start_desk()
    show_desk(example)
    loop()
    while True:
        repeat = ''
        while repeat.lower() not in ['yes', 'no']:
            repeat = input('Желаете повторить? (Yes / No)')
        if repeat.lower() == 'yes':
            loop()
        else:
            print('Спасибо за игру')
            break


game()
