def bubble_sort(list):
    for index in range(len(list)-1):
        for index2 in range(len(list)-1-index):
            if list[len(list)-1-index2]<list[len(list)-2-index2]:
                temporary=list[len(list)-1-index2]
                list[len(list)-1-index2]=list[len(list)-2-index2]
                list[len(list)-2-index2]=temporary
    return list

#Main
list=[100,5,46,1,24,73,12,31,58]
print(bubble_sort(list))