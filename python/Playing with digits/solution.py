def dig_pow(n, p):
    dig_as_str = str(n)
    res = 0
    for i in dig_as_str:
        res += int(i) ** p
        p += 1
    k = res / n
    if res % n == 0:
        return k
    return -1
