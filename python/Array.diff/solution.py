def array_diff(a, b):
    for item_b in b:
        while item_b in a: a.remove(item_b)
    return a
