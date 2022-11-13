def narcissistic(value):
    size = len(str(value))
    result = 0
    for i in str(value):
        result = int(i) ** size
    return result == int(value)
