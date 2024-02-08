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
