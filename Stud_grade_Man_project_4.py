#Initializing Dictionary

student_grade = {  }

#Add a new Student
def  add_Student(name,grade):
    student_grade[name] = grade
    #[nidhesh] = 100
    print(f"Added {name} with a {grade}")
    #Added nidhesh with a 100


#Update a Student
def update_student(name,grade):
    if name in student_grade:
        student_grade[name] = grade
        #nidhesh = 200

        print(f"Updated {name} with a {grade}")
    else:
        print(f"{name} is not found")

def delete_student(name):
    if name in student_grade:
        del student_grade[name]
        print(f"{name} has been deleted successfully")

    else:
        print(f"{name} is not found")


def display_student():
    if student_grade:
        for name,garde in student_grade.items():
            print(f"{name} : {garde}")        
    else:
            print(f"No student found/added")


def main():
    while True:
        print("\n Student Grade System.....")            
        print("YOU WANT TO ADDED A STUDENT: [PRESS 1]")            
        print("YOU WANT TO UPDATE A STUDENT: [PRESS 2]")            
        print("YOU WANT TO DELETE A STUDENT: [PRESS 3]")            
        print("YOU WANT TO DISPLAY ALL  STUDENT WITH GRADES: [PRESS 4]")            
        print("PRESS 5 (EXIT TO QUIT THE APP)") 

        choice = int(input("Enter Your Choice: "))
    
        if choice == 1:
             print(f"\n\tGive Following Information  Plz...") 
             name = input("Enter the student name: ")
             grade = int(input("Enter Student grade: "))
             add_Student(name,grade)

        elif choice == 2:
             print(f"\n\tGive Following Information  for Update Plz...") 
             name = input("Enter the student name: ")
             grade = int(input("Enter Student grade: "))
             update_student(name,grade)
            

        elif choice == 3:
             print(f"\n\tGive Following Information  to Delete Record Plz...") 
             name = input("Enter the student name: ")
             delete_student(name)

        elif choice == 4:
            print("\n\tAll Student List.....") 
            display_student()

        elif choice == 5:
             print("\n\ttClosing the program.....")
             break
         
        else:
            print("\n\tInvalid input plz Pefer Above given Information")            


if __name__ == "__main__":

  main()

                    

