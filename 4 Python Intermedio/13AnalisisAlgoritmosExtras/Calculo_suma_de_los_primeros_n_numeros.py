def manual_add(number):
    result = 0  # O(1)
    for i in range(1, number + 1):  # O(n)
        result += i  # O(1)
    return result  # O(1)

def add_formula(number):
    return number * (number + 1) // 2  # O(1)


# Response #1:
# Complexity manual add # O(n)
# Complexity add_formula # O(1)

# Response #2:
# Considering only one cycle is required in algorithm #2 to get answer,
# I choose option add_formula algorithm