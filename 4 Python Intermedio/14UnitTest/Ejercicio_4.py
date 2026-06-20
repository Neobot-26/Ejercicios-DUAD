def new_string(my_sentence):
    index=0
    new_sentence = ""
    while (index < len(my_sentence)):
        new_sentence = new_sentence + my_sentence[len(my_sentence) - index-1]
        index += 1
    return new_sentence


#main
my_string= "Hola mundo!!!"
print(f"La oración alrevés es: {new_string(my_string)}")