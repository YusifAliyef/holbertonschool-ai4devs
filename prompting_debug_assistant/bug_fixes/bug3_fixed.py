def parse_user_data(data_string):
    """
    Parses comma-separated user data string safely.
    Fixed with length and format validation.
    """
    if not data_string or "," not in data_string:
        return None
        
    parts = data_string.split(",")
    if len(parts) < 2:
        return None
        
    username = parts[0].strip()
    try:
        age = int(parts[1].strip())
    except ValueError:
        age = 0
        
    return {
        "username": username,
        "age": age
    }
