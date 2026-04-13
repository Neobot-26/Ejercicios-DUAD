import actions
def menu_options():
    file_path='students_register.csv'
    list_of_dictionary=[]
    list_of_headers=["name","classroom","score_spanish","score_english","score_history","score_science","average"]
    while True:
        try:
            print("1. Enter Information for a new student")
            print("2. See Information for all students")
            print("3. See Top 3 students")
            print("4. See average score of students")
            print("5. Export Data to CSV file")
            print("6. Import Data from CSV file")
            print("7. Delete student from Register")
            print("8. See list of students who failed")
            print("9. Exit")
            option_selected=int(input("Select option:"))
            if option_selected==1:  
                print("Entering Information for a new Student")
                actions.create_student(list_of_dictionary)
            elif option_selected==2:
                print("2. Reviewing Information for all students")
                actions.students_read(list_of_dictionary)
            elif option_selected==3: 
                print("Seeing Top 3 students")
                actions.student_top_three_average(list_of_dictionary)
            elif option_selected==4: 
                print("Seeing average score of students")
                actions.student_average(list_of_dictionary)
            elif option_selected==5:
                print("Exporting Data to CSV file")
                actions.export_data(file_path,list_of_headers,list_of_dictionary)
            elif option_selected==6:
                print("Importing Data from CSV file")
                list_of_dictionary=actions.import_data(file_path,list_of_dictionary)
            elif option_selected==7:
                print("Deleting student from Register")
                actions.student_delete(list_of_dictionary)
            elif option_selected==8:   
                print("Seeing list of students who failed")
                actions.students_under_sixty(list_of_dictionary)
            elif option_selected==9:
                break        
            else:
                print("Invalid option, select correct option")
        except ValueError as e:
            print(f"Error [ValueError]: Unable to convert the value 'abc' to integer. Details:{e}")