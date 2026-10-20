
def bubble_sort(list):
    for index in range(len(list)-1): # O(n)
        for index2 in range(len(list)-1-index): # O(n^2)
            if list[index2]>list[index2+1]: # O(1)
                temporary=list[index2] # O(1)
                list[index2]=list[index2+1] # O(1)
                list[index2+1]=temporary # O(1)
    return list # O(1)

#Main
list=[100,5,46,1,24,73,12,31,58] # O(1)
print(bubble_sort(list)) # O(1)

#Algorithm has a complexity type O(n^2)