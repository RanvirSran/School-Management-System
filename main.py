from management import Management
from initializer import Initializer

# SOME CONSTANTS
choice_dict = {
    1: "STUDENT MANAGEMENT",
    2: "EMPLOYEE MANAGEMENT",
    3: "FEE MANAGEMENT",
    4: "EXAM MANAGEMENT"
}
choice = None

# PRINT PROJECT DETAILS
print("\t\t\t\t Modern Senior Secondary School, Patiala")
print("\t\t\t\t _______________________________________")
print("\n\t\t\t\t\t\t School Management System")
print("\t\t\t\t\t\t ________________________\n")
print("\t\t\t Created by Ranvir, Vinayak, Chetan     ||     Class XII \n\n")

# CHECK IF DATABASE AND TABLES ARE THERE
Initializer()

# MAIN PROGRAM START
print("-----------------------------------")
print("WELCOME TO SCHOOL MANAGEMENT SYSTEM")
print("-----------------------------------")

# RECURSION UNTIL USER DECIDES TO EXIT
while choice != 5:
    try:
        choice = int(input("1.STUDENT MANAGEMENT \n2.EMPLOYEE MANAGEMENT \n3.FEE MANAGEMENT \n4.EXAM MANAGEMENT "
                            "\n5.EXIT \n\nEnter your choice (1-5): "))
    except:
        print("Invalid Input, Try again \n\n")
    else:
        # REFER TO management.py FOR WHAT HAPPENS NEXT
        Management(choice_dict[choice])
