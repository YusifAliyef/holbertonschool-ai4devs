def get_last_n_items(items, n):
    """
    Retrieves the last n items from a given list correctly.
    Fixed using proper slicing.
    """
    if n <= 0:
        return []
    return items[-n:]
