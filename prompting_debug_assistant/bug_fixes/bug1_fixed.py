def get_last_n_items(items, n):
    """
    Retrieves the last n items from a given list correctly.
    Fixed using proper slicing to avoid index out of bounds.
    This function ensures safety and correct data extraction.
    """
    if n <= 0:
        return []
    
    # Return the last n items using Python negative slicing
    return items[-n:]
