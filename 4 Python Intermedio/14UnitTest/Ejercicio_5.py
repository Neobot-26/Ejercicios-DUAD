def new_string(my_sentence):
    index=0
    lower_case = 0
    upper_case = 0
    special_character = 0
    while (index < len(my_sentence)):
        if my_sentence[index].isupper():
            upper_case +=1
        elif my_sentence[index].islower():
            lower_case +=1
        else:
            special_character += 1
        index += 1
    return lower_case, upper_case


#main
upper_case=0
lower_case=0
my_string= "Hola Mundo!!!"
lower_case,upper_case = new_string(my_string)
print(f"There´s {upper_case} upper cases and {lower_case} lower cases")