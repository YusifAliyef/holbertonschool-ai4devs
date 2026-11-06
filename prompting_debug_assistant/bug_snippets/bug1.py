def get_last_n_items(items, n):
    # Bug: range goes out of bounds or slicing logic misses items when n == len(items)
    result = []
    for i in range(n + 1):
        result.append(items[len(items) - i])
    return result
