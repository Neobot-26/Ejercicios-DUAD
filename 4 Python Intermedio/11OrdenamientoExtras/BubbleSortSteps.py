def bubble_sort_steps(list):
    counter_interchanges=0
    counter_iterations=0
    for index in range(len(list)-1):
        for index2 in range(len(list)-1-index):
            if list[index2]>list[index2+1]:
                temporary=list[index2]
                list[index2]=list[index2+1]
                list[index2+1]=temporary
                counter_interchanges+=1
        counter_iterations+=1
    print(f"Sorted List:{list}")
    print(f"Iterations:{counter_iterations}")
    print(f"Interchanges:{counter_interchanges}")

#Main
list=[100,5,46,1,24,73,12,31,58]
bubble_sort_steps(list)