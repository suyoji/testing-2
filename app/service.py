def greet(name):
    return f"hello {name}"


def farewell(name):
    return f"bye {name}"


def whisper(name):
    return greet(name).lower()
