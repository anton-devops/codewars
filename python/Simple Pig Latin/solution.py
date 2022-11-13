def pig_it(text):
    result = ''
    punctuation = [',', '!', '.', ':', '?']
    for i in text.split():
        if i in punctuation:
            result += f'{i} '
        else:
            result += f'{i[1:] + i[:1]}ay '
    return result[:-1]
