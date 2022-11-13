def tower_builder(n_floors):
    tower = [("*" * (2 * i - 1)).center(2 * n_floors - 1) for i in range(1, n_floors + 1)]
    return tower
