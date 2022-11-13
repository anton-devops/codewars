def increment_string(strng):
    head = strng.rstrip('0123456789')
    print(head)
    tail = strng[len(head):]
    print(tail)
    if tail == "":
        return strng + "1"
    return head + str(int(tail) + 1).zfill(len(tail))
