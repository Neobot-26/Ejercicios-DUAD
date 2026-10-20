def linear_search(my_list, target):
    for item in my_list:  # O(n)
        if item == target:  # O(1)
            return True  # O(1)
    return False  # O(1)


def binary_search(my_list, target):
    low = 0   # O(1)
    high = len(my_list) - 1  # O(1)
    while low <= high:  # O(log n)
        mid = (low + high) // 2  # O(1)
        if my_list[mid] == target:  # O(1)
            return True  # O(1)
        elif my_list[mid] < target:  # O(1)
            low = mid + 1  # O(1)
        else:
            high = mid - 1  # O(1)
    return False  # O(1)

# Response 1:
# Complexity Linear_search= O(n)
# Complexity Binary_search= O(log n)

# Response 2:
# Linear_Search is more convenient to be used if the list is not sorted
# Binary_Search is more convenient to be used if the list is sorted

# Response 3:
# If the list is not sorted the function can return wrong answers 
