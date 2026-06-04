def bubble_sort(list):
    for index in range(len(list)-1):
        for index2 in range(len(list)-1-index):
            if list[index2]<list[index2+1]:
                temporary=list[index2]
                list[index2]=list[index2+1]
                list[index2+1]=temporary
    return list

#Main
list=[100,5,46,1,24,73,12,31,58]
print(bubble_sort(list))