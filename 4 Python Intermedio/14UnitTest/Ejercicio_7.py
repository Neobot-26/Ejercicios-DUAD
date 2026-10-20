def prime_numbers(new_number):
    flag=0
    if new_number<=1:
        return flag
    elif new_number==2:
        flag=1
        return flag
    elif new_number>2 and new_number%2==0:
        return flag
    for index in range(3,new_number):
        if new_number%index==0:
            return flag
    flag=1
    return flag

def verification(new_list):
    prime_list=[]
    for index in range(len(new_list)):
        if prime_numbers(new_list[index])==1:
            prime_list.append(new_list[index])
    return prime_list

#main
my_list=[1, 4, 7, 13, 9, 67, 2, 31, 57, 29, 51]
print(verification(my_list))
