
def validate_numbers(func):
    def wrapper(*args, **kwargs):
        # Validate parameters positionals
        for value in args:
            if not isinstance(value, (int, float)):
                raise ValueError(
                    f"The value '{value}' is not a number"
                )

        # Validate parameters named
        for key, value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise ValueError(
                    f"The parameter '{key}' with value '{value}' is not a number"
                )

        return func(*args, **kwargs)

    return wrapper


# =========================
# Example of use
# =========================

@validate_numbers
def multiply(a, b):
    return a * b


@validate_numbers
def average(a, b, c=0):
    return (a + b + c) / 3


print(multiply(5, 4))

print(average(10, 20, c=60))

# Exception
print(multiply(5, "8"))