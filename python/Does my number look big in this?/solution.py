def narcissistic(value):
    num_of_digits = len(str(value))
    result = 0
    for i in str(value):
        result += int(i) ** num_of_digits
    if result == value:
        return True
    return False
