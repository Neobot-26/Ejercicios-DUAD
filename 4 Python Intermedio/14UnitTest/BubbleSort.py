def bubble_sort(list_to_order):
    for index in range(len(list_to_order)-1):
        for index2 in range(len(list_to_order)-1-index):
            if list_to_order[index2]>list_to_order[index2+1]:
                temporary=list_to_order[index2]
                list_to_order[index2]=list_to_order[index2+1]
                list_to_order[index2+1]=temporary
    return list_to_order

#Main
list=[100,5,46,1,24,73,12,31,58]
print(bubble_sort(list))