def expanded_form(num):
    result = ''
    size = len(str(num))

    for i in str(num):
        if int(i) != 0:
            result += f'{int(i) * 10 ** (size - 1)} + '
        size -= 1
    return result[:-3]
