import data

def student_register(list_of_dictionary,list_of_headers):
    while True:
        try:
            list_of_info=[]
            dictionary_student={}
            name_student=input("Enter name of student:")
            while is_valid_name(name_student)==1:
                print("Text entered for name is not valid, enter a valid name")
                name_student=input("Enter name of student:")
            classroom_student=input("Enter classroom of student:")
            while is_valid_classroom(classroom_student)==1:
                print("Text entered for Classroom is not valid, enter a valid data")
                classroom_student=input("Enter classroom of student:")
            if student_in_class(list_of_dictionary,name_student,classroom_student)==0:
                list_of_info.append(name_student)
                list_of_info.append(classroom_student)
                spanish_score=subject_matter("Spanish")
                list_of_info.append(spanish_score)
                english_score=subject_matter("English")
                list_of_info.append(english_score)
                history_score=subject_matter("History")
                list_of_info.append(history_score)
                science_score=subject_matter("Science")
                list_of_info.append(science_score)
                list_of_info.append((spanish_score+english_score+history_score+science_score)/4)
                index_info=0
                for index_header in list_of_headers:
                    dictionary_student[index_header]=list_of_info[index_info]
                    index_info+=1
                list_of_dictionary.append(dictionary_student)
            else:
                print("Student already exists in classroom...")
            cycle=input("Would you like to add a new register?Y/N:")
            if cycle == "N" or cycle == "n":
                return list_of_dictionary
                break
        except ValueError as e:
            print(f"Error [ValueError]: Unable to convert the value 'abc' to integer. Details:{e}")
            print("Re-enter information of Student")

def student_in_class(dictionary_students,name,classroom):
    student_exist=0
    for row in dictionary_students:
        if row["name"]==name and row["classroom"]==classroom:
            student_exist=1
    return student_exist


def student_delete(list_of_dictionary,list_of_headers):
    try:
        name_student=input("Enter name of student to delete:")
        while is_valid_name(name_student)==1:
            print("Text entered for name is not valid, enter a valid name")
            name_student=input("Enter name of student to delete:")
        classroom_student=input("Enter classroom of student to delete:")
        while is_valid_classroom(classroom_student)==1:
            print("Text entered for Classroom is not valid, enter a valid data")
            classroom_student=input("Enter classroom of student to delete:")
        if student_in_class(list_of_dictionary,name_student,classroom_student)==1:
            confirm_delete=input("Student exists in registers, would you like to proceed, Y/N:")
            if confirm_delete=="Y" or confirm_delete=="y":
                list_of_dictionary=proceed_delete_student(list_of_dictionary,name_student,classroom_student)
                return list_of_dictionary
        else:
            print("Student is not present is registers")
    except ValueError as e:
            print(f"Error [ValueError]: Unable to convert the value 'abc' to integer. Details:{e}")
            print("Re-enter information of Student")


def students_read(list_of_dictionary,list_of_headers):
    try:
        for row in list_of_dictionary:
            index=0
            for index in range(len(list_of_headers)-1):
                print(f"{list_of_headers[index].capitalize()}: {row[list_of_headers[index]]}")
            print(" ")
    except ValueError as e:
        print(f"Error [ValueError]: Unable to convert the value 'abc' to integer. Details:{e}")
        print("There is Information of Students")
        
def student_average(list_of_dictionary,list_of_headers):
    sum_total=0
    counter_of_notes=0
    average_total=0
    for row in list_of_dictionary:
        sum_total=sum_total+float(row[list_of_headers[6]])
        counter_of_notes+=1
    average_total=sum_total/counter_of_notes
    print(f"Total Average of Students: {average_total}")
    print(" ")    

def student_top_three_average(list_of_dictionary):
    num_register=0
    qty_register=0
    names_list=[]
    top_three=[]
    for row in list_of_dictionary:
        names_list.append(row['name'])
        top_three.append(float(row['average']))
    for index_list1 in range(len(names_list)-1):
        for index_list2 in range(len(names_list)-1-index_list1):
            if top_three[index_list2]<top_three[index_list2+1]:
                aux_variable=top_three[index_list2]
                top_three[index_list2]=top_three[index_list2+1]
                top_three[index_list2+1]=aux_variable
                aux_name=names_list[index_list2]
                names_list[index_list2]=names_list[index_list2+1]
                names_list[index_list2+1]=aux_name
    if len(names_list)<3:
        qty_register=len(names_list)
    else:
        qty_register=3
    while num_register<qty_register:
        print(f"Name:{names_list[num_register]}")
        print(f"Average:{top_three[num_register]}")
        print(" ")
        num_register+=1

def is_valid_name(name):
    valid_name=0
    if name==" ":
        valid_name=1
    else:
        if not name.replace(" ","").isalpha():
            valid_name=1
    return valid_name

def is_valid_classroom(classroom):
    valid_classroom=0
    if classroom==" ":
        valid_classroom=1
    elif len(classroom)!=3:
        valid_classroom=1    
    elif not classroom[0].isdigit() or not classroom[1].isdigit() or not classroom[2].isalpha():
            valid_classroom=1
    return valid_classroom

def is_valid_score(score):
    valid_score=0
    if score==" ":
        valid_score=1
    elif score<0 or score>100:
        valid_score=1
    return valid_score

def students_under_sixty(dictionary,head_list):
    quantity_of_students=0
    for row in dictionary:
        spanish_flag=0
        english_flag=0
        history_flag=0
        science_flag=0
        for index in range(2,6):
            if int(row[head_list[index]])<60:
                if index==2:
                    spanish_flag=1
                elif index==3:
                    english_flag=1
                elif index==4:
                    history_flag=1
                elif index==5:
                    science_flag=1
                quantity_of_students=1
        if spanish_flag==1 or english_flag==1 or history_flag==1 or science_flag==1:
            print(f"{head_list[0].capitalize()}: {row['name']}")
            print(f"{head_list[1].capitalize()}: {row['classroom']}")
            if spanish_flag==1:
                print(f"{head_list[2].capitalize()}: {row['score_spanish']}")
            if english_flag==1:    
                print(f"{head_list[3].capitalize()}: {row['score_english']}")
            if history_flag==1:
                print(f"{head_list[4].capitalize()}: {row['score_history']}")
            if science_flag==1:
                print(f"{head_list[5].capitalize()}: {row['score_science']}")
    if quantity_of_students==0:
        print("There are not failing students in registers")

def subject_matter(field_of_study):
    subject_score=int(input(f"Enter {field_of_study} Score:"))
    while is_valid_score(subject_score)==1:
        print("Score not valid, enter a valid score")
        subject_score=int(input(f"Enter {field_of_study} Score:"))
    return subject_score

def proceed_delete_student(list_of_dictionary,name,classroom):
    register_students=[]
    try:
        for row in list_of_dictionary:
            if row['name'] != name or row['classroom'] != classroom:
                register_students.append(row)
        list_of_dictionary=register_students
        return list_of_dictionary
    except ValueError as e:
        print(f"Error [ValueError]: Unable to convert the value 'abc' to integer. Details:{e}")
        print("There is not information of Students")

def export_data(file_name,list_of_headers,data_students):
    new_database="Y"
    if data.verification_csv_file(file_name)!=0:
        print("-"*60)
        new_database=input("File does not exist, would you like to create a new database? Y/N:")
        print("-"*60)
    if new_database=="y" or new_database=="Y":
        data.write_csv_filedata(file_name,list_of_headers,data_students)

def import_data(file_name,data_students):
    if data.verification_csv_file(file_name)!=0:
        print("-"*60)
        print("File with information does not exist, unable to import data")
        print("-"*60)
    else:
        data_students=data.read_csv_file(file_name)
        return data_students