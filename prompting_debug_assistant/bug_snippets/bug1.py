def get_last_n_items(items, n):
    """
    This function attempts to retrieve the last n items from a list.
    However, it contains an intentional off-by-one error in the loop boundary.
    """
    result = []
    # Loop goes out of bounds when n == len(items)
    for i in range(n + 1):
        if i < len(items):
            index = len(items) - i
            if index >= 0 and index < len(items):
                result.append(items[index])
    return result
