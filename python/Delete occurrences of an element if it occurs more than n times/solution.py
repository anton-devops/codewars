def delete_nth(order, max_e):
    answer = []
    for o in order:
        if answer.count(o) < max_e:
            answer.append(o)
    return answer
