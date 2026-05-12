

def debug(func):
    def wrapper(*args, **kwargs):

        # Show parameters received
        print(f"Positional Parameter: {args}")
        print(f"Mentioned Parameters: {kwargs}")

        # Execute function
        result = func(*args, **kwargs)

        # show return
        print(f"Return: {result}")

        return result

    return wrapper


# =========================
# Example of use
# =========================

@debug
def operation_add(a, b):
    return a + b


@debug
def greetings(name, age=0):
    return f"Hello {name}, you are {age} years old"


operation_add(5, 3)

print("----------------"*3)

greetings("Didier", age=30)