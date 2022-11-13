def choose_best_sum(t, k, ls):

    def combinations(array, k):
        n = len(array)
        result = []
        if k == 0:
            return [[]]
        for i in range(n):
            for p in combinations(array[i + 1:], k - 1):
                result.append([array[i], *p])
        return result

    diff_res = []
    for combination in combinations([i for i in range(len(ls))], k):
        result = [ls[i] for i in combination]
        diff = t - sum(result)
        if diff >= 0:
            # print(result, sum(result))
            diff_res.append(sum(result))
    if not diff_res:
        return None
    return max(diff_res)
