def validate_battlefield(field):
    RIGHT_CELLS = 20
    if sum([line.count(1) for line in field]) != RIGHT_CELLS:
        return False
    field_size = len(field)

    battleship = 0
    cruisers = 0
    destroyers = 0
    submarines = 0

    for x in range(field_size):
        try:
            for y in range(field_size):
                count_x = count_y = 0
                while field[y + count_y][x] == 1:
                    count_y += 1
                while field[y][x + count_x] == 1:
                    count_x += 1
                if count_x > 4 or count_y > 4:
                    return False
                if count_x > 1 and count_y > 1:
                    return False
                if field[y][x] \
                        + field[y + 1][x + 1] \
                        + field[y + 1][x] \
                        + field[y][x + 1] > 2 \
                        or field[y][x] == field[y + 1][x + 1] == 1 \
                        or field[y][x + 1] == field[y + 1][x] == 1:
                    return False
                if (count_x == 4 and count_y == 1) or (count_y == 4 and count_x == 1):
                    battleship += 1
                if (count_x == 3 and count_y == 1) or (count_y == 3 and count_x == 1):
                    cruisers += 1
                if (count_x == 2 and count_y == 1) or (count_y == 2 and count_x == 1):
                    destroyers += 1
                if count_x == 1 and count_y == 1:
                    submarines += 1
        except:
            continue
    if battleship > 1:
        return False
    return True


if __name__ == '__main__':
    battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                   [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                   [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    if validate_battlefield(battleField):
        print('OK')
    else:
        print('Failed')
