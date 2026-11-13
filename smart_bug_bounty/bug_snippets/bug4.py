def add_tag(tag, tags=[]):
    """Return a new list of tags that contains the given tag."""
    tags.append(tag)
    return tags


def describe(tags):
    return ", ".join(tags)


def main():
    post1 = add_tag("python")
    post2 = add_tag("java")
    print(describe(post1))  # expected: python
    print(describe(post2))  # expected: java


if __name__ == "__main__":
    main()
