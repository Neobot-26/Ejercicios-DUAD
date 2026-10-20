def is_numeric(value):
    try:
        int(value)
        return True
    except (ValueError, TypeError):
        return False
    
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

def validate_data(list):
    if not list:
        return False
    for index_data in range(len(list)):
        if not is_numeric(list[index_data]):
            return False
    return True

#Main
list=[100,5,46,1,"a",24,73,12,31,58]
#list=[]
#list=[100,5,46,1,24,73,12,31,58]
if validate_data(list):
    bubble_sort_steps(list)
else:
    print("Error: The list contains not numeric elements")