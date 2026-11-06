def parse_user_data(data_string):
    """
    Parses comma-separated user data.
    Raises IndexError or KeyError if format is invalid.
    """
    parts = data_string.split(",")
    username = parts[0].strip()
    age = int(parts[1].strip())
    return {
        "username": username,
        "age": age
    }
