def is_valid_walk(walk):
    up = walk.count("n")
    down = walk.count('s')
    right = walk.count('e')
    left = walk.count('w')

    return len(walk) == 10 and up == down and left == right
