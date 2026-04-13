import data

class Student():    #Class created to manage information of students
    def __init__(self,name,classroom,spanish_score,english_score,history_score,science_score,average_score):
        self.name = name
        self.classroom = classroom
        self.spanish_score = spanish_score
        self.english_score = english_score
        self.history_score = history_score
        self.science_score = science_score
        self.average_score = average_score

def student_delete(list_of_data):   #This function is used to delete students from registers if they exist
    try:
        name_student=input("Enter name of student to delete:")
        while is_valid_name(name_student)==1:
            print("Text entered for name is not valid, enter a valid name")
            name_student=input("Enter name of student to delete:")
        classroom_student=input("Enter classroom of student to delete:")
        while is_valid_classroom(classroom_student)==1:
            print("Text entered for Classroom is not valid, enter a valid data")
            classroom_student=input("Enter classroom of student to delete:")
        if student_in_class(list_of_data,name_student,classroom_student)==1:
            confirm_delete=input("Student exists in registers, would you like to proceed, Y/N:")
            if confirm_delete=="Y" or confirm_delete=="y":
                for row_index in list_of_data:
                    if row_index.name == name_student and row_index.classroom == classroom_student:
                        list_of_data.remove(row_index)
        else:
            print("Student is not present in registers")
    except ValueError as e:
            print(f"Error [ValueError]: Unable to convert the value 'abc' to integer. Details:{e}")
            print("Re-enter information of Student")

def create_student(list_of_data):   #This function is used to register a new student in records
    while True:
        try:
            name_student=input("Enter name of student:")
            while is_valid_name(name_student)==1:
                print("Text entered for name is not valid, enter a valid name")
                name_student=input("Enter name of student:")
            classroom_student=input("Enter classroom of student:")
            while is_valid_classroom(classroom_student)==1:
                print("Text entered for Classroom is not valid, enter a valid data")
                classroom_student=input("Enter classroom of student:")
            if student_in_class(list_of_data,name_student,classroom_student)==0:
                spanish_score=subject_matter("Spanish")
                english_score=subject_matter("English")
                history_score=subject_matter("History")
                science_score=subject_matter("Science")
                average_score=(spanish_score+english_score+history_score+science_score)/4
                list_of_data.append(Student(name_student,classroom_student,spanish_score,english_score,history_score,science_score,average_score))
            else:
                print("Student already exists in classroom...")
            cycle=input("Would you like to add a new register?Y/N:")
            if cycle == "N" or cycle == "n":
                return list_of_data
                break
        except ValueError as e:
            print(f"Error [ValueError]: Unable to convert the value 'abc' to integer. Details:{e}")
            print("Re-enter information of Student")

def is_valid_name(name_student):    #This function is used to verify if a name of student includes correct format.
    valid_name=0
    if name_student==" ":
        valid_name=1
    else:
        if not name_student.replace(" ","").isalpha():
            valid_name=1
    return valid_name

def is_valid_classroom(classroom): #This function is used to verify if a classroom of student includes correct format.
    valid_classroom=0
    if classroom==" ":
        valid_classroom=1
    elif len(classroom)!=3:
        valid_classroom=1    
    elif not classroom[0].isdigit() or not classroom[1].isdigit() or not classroom[2].isalpha():
        valid_classroom=1
    return valid_classroom

def student_in_class(info_of_students,name,classroom):  #This function is used to verify if student is inside of the registers
    student_exist=0
    for row in info_of_students:
        if row.name==name and row.classroom==classroom:
            student_exist=1
    return student_exist

def subject_matter(field_of_study):     #This function is used to verify if score of student includes correct format.
    subject_score=int(input(f"Enter {field_of_study} Score:"))
    while is_valid_score(subject_score)==1:
        print("Score not valid, enter a valid score")
        subject_score=int(input(f"Enter {field_of_study} Score:"))
    return subject_score

def is_valid_score(score):   #This function is used to verify score of student includes correct format.
    valid_score=0
    if score==" ":
        valid_score=1
    elif score<0 or score>100:
        valid_score=1
    return valid_score

def student_average(list_of_students):  #This function is used to calculate average of scores of all students.
    sum_total=0
    counter_of_notes=0
    average_total=0
    for row_index in list_of_students:
        sum_total=sum_total+float(row_index.average_score)
        counter_of_notes+=1
    average_total=sum_total/counter_of_notes
    print(f"Total Average of Students: {average_total}")
    print("_____________________")  

def student_top_three_average(list_of_students):   #This function is used to find students with highest scores
    num_register=0
    qty_register=0
    names_list=[]
    top_three=[]
    for row_index in list_of_students:
        names_list.append(row_index.name)
        top_three.append(float(row_index.average_score))
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
        print("_____________________")
        num_register+=1

def students_read(list_of_data):     #This function is used to show information of students
    try:
        for row_of_list in list_of_data:
            print(f"Name:{row_of_list.name}")
            print(f"Classroom:{row_of_list.classroom}")
            print(f"Score Spanish:{row_of_list.spanish_score}")
            print(f"Score English:{row_of_list.english_score}")
            print(f"Score History:{row_of_list.history_score}")
            print(f"Score Science:{row_of_list.science_score}")
            print("_____________________")
    except ValueError as e:
        print(f"Error [ValueError]: Unable to convert the value 'abc' to integer. Details:{e}")
        print("There is Information of Students")

def students_under_sixty(list_of_data):      #This function is used to show information of students with scores under 60
    quantity_of_students=0
    for row_of_list in list_of_data:
        if int(row_of_list.spanish_score)<60 or int(row_of_list.english_score)<60 or  int(row_of_list.history_score)<60 or int(row_of_list.science_score)<60:   
            print(f"Name:{row_of_list.name}")
            print(f"Classroom:{row_of_list.classroom}")
            print(f"Score Spanish:{row_of_list.spanish_score}")
            print(f"Score English:{row_of_list.english_score}")
            print(f"Score History:{row_of_list.history_score}")
            print(f"Score Science:{row_of_list.science_score}")
            print("_____________________")
            quantity_of_students+=1
    if quantity_of_students==0:
        print("There are not failing students in registers")


def export_data(file_name,list_of_headers,data_students):
    new_database="Y"
    list_of_dictionary=[]
    if data.verification_csv_file(file_name)!=0:
        print("-"*60)
        new_database=input("File does not exist, would you like to create a new database? Y/N:")
        print("-"*60)
    if new_database=="y" or new_database=="Y":
        for row in data_students:
            list_of_info=[]
            dictionary_student={}
            list_of_info.append(row.name)
            list_of_info.append(row.classroom)
            list_of_info.append(row.spanish_score)
            list_of_info.append(row.english_score)
            list_of_info.append(row.history_score)
            list_of_info.append(row.science_score)
            list_of_info.append(row.average_score)
            index_info=0
            for index_header in list_of_headers:
                dictionary_student[index_header]=list_of_info[index_info]
                index_info+=1
            list_of_dictionary.append(dictionary_student)
        data.write_csv_filedata(file_name,list_of_headers,list_of_dictionary)

def import_data(file_name,data_students):
    if data.verification_csv_file(file_name)!=0:
        print("-"*60)
        print("File with information does not exist, unable to import data")
        print("-"*60)
    else:
        data_students.clear()
        data_from_csv=data.read_csv_file(file_name)
        for row in data_from_csv:
            student = Student(row["name"],row["classroom"],row["score_spanish"],row["score_english"],row["score_history"],row["score_science"],row["average"])
            data_students.append(student)
        return data_students