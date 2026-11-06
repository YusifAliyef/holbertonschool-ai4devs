def parse_user_data(data_string):
    # Bug: assumes key always exists, causes KeyError if missing
    user = data_string.split(",")
    age = int(user[1])
    return {"username": user[0], "age": age}
