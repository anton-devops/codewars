def persistence(n):
    count = 0
    str_n = str(n)

    while len(str_n) > 1:
        result = 1
        for i in str(str_n):
            result *= int(i)
        str_n = str(result)
        count += 1

    return count
