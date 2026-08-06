def sum_values(my_list):
    index=0
    sumatory = 0
    while (index < len(my_list)):
        sumatory = sumatory + my_list[index]
        index += 1
    return sumatory


#main
my_list=[16, 23, 67, 6, 34]
print(f"La suma de los valores de la lista es: {sum_values(my_list)}")