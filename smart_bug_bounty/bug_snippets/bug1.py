def last_n_items(items, n):
    """Return the last n items of a list."""
    if n <= 0:
        return []
    if n >= len(items):
        return list(items)
    return items[-(n + 1):]


def main():
    data = [1, 2, 3, 4, 5]
    print(last_n_items(data, 2))   # expected [4, 5]
    print(last_n_items(data, 0))   # expected []
    print(last_n_items(data, 10))  # expected [1, 2, 3, 4, 5]


if __name__ == "__main__":
    main()
