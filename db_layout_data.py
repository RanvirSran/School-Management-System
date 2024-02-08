# DB'S GENERAL LAYOUT DETAILS TO USE IN MODULE
data_dict = {
    "STUDENT MANAGEMENT": {
        "Options": ["1. NEW ADMISSION", "2. UPDATE STUDENT DETAILS", "3. ISSUE TC", "4. DISPLAY STUDENT DETAILS"],
        "DB_Name": "Students",
        "DB_Fields": ["AdmNo", "StudentName", "DOB", "Class"],
        "Respective Queries": ["Student Name", "Date of Birth", "Class"]
        },
    "EMPLOYEE MANAGEMENT": {
        "Options": ["1. NEW EMPLOYEE", "2. UPDATE STAFF DETAILS", "3. DELETE EMPLOYEE DETAILS",
                    "4. DISPLAY STAFF DETAILS"],
        "DB_Name": "Employees",
        "DB_Fields": ["EmpNo", "EmployeeName", "HireDate", "Job"],
        "Respective Queries": ["Employee Name", "Date of Hire", "Job"]
    },
    "FEE MANAGEMENT": {
        "Options": ["1. ADD DUE FEE", "2. UPDATE FEE AMOUNT", "3. EXEMPT FEE", "4. DISPLAY FEE DETAILS"],
        "DB_Name": "Fee",
        "DB_Fields": ["SrNo", "StudentName", "Month", "Fee"],
        "Respective Queries": ["Student Name", "Month", "Fee Due"]
    },
    "EXAM MANAGEMENT": {
        "Options": ["1. EXAM DETAILS", "2. UPDATE ASSESSMENT", "3. DELETE DETAILS", "4. DISPLAY RESULT DETAILS"],
        "DB_Name": "Exam",
        "DB_Fields": ["SrNo", "StudentName", "Obtained", "Total"],
        "Respective Queries": ["Student Name",  "Marks Obtained", "Total Marks"]
    }
}
