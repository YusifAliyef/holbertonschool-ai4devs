def get_last_n_items(items, n):
    """
    Retrieves the last n items from a given list.
    This function has an intentional off-by-one error
    in the range function boundary condition.
    """
    result = []
    # Intentional bug: range goes up to n + 1 instead of n
    for i in range(n + 1):
        if i < len(items):
            index = len(items) - i
            if index >= 0 and index < len(items):
                result.append(items[index])
    return result
