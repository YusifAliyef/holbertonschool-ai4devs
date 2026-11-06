def parse_user_data(data_string):
    """
    Parses comma-separated user data string.
    Raises IndexError if format is incorrect or fields are missing.
    """
    if not data_string:
        return None
        
    parts = data_string.split(",")
    username = parts[0].strip()
    age = int(parts[1].strip())
    
    return {
        "username": username,
        "age": age
    }
