def print_all_pairs(my_dict):
    for key1 in my_dict:   # O(n)
        for key2 in my_dict:  # O(n^2)
            print(f"{key1}-{key2}") # O(1)

# Response 1: Temporal complexity is O(n^2)
# Response 2: This function requires 1.000.000^2 of cycles.