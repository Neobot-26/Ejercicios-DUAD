def string_to_list(my_sentence):
    my_list=[]
    index=0
    aux_string = ""
    while (index < len(my_sentence)):
        if my_sentence[index]=="-":
            my_list.append(aux_string)
            aux_string=""
        else:
            aux_string=aux_string+my_sentence[index]
        index += 1
    my_list.append(aux_string)
    return my_list

def sort_list(my_list):
    for index_ext in range(len(my_list)):
        for index in range(1,len(my_list)-index_ext):
            Temp_string = my_list[index-1]
            if my_list[index]<Temp_string:
                my_list[index-1]=my_list[index]
                my_list[index]=Temp_string
    return my_list       

def list_to_string(my_list):
    aux_string=my_list[0]
    for index in range(1,len(my_list)):
        aux_string=aux_string+"-"+my_list[index]
    return aux_string

#main
aux_list = []
second_list=[]
my_string= "python-variable-funcion-computadora-monitor"
aux_list = string_to_list(my_string)
second_list = sort_list(aux_list)
print(list_to_string(second_list))