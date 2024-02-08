import mysql.connector as sql


class Initializer:
    def __init__(self):
        # CREATING DATABASE AND REQUIRED TABLES
        db = sql.connect(host="localhost", user="Ranvir", passwd="ranvir_sran")
        mycursor = db.cursor()
        print(" Creating Database")
        mycursor.execute("CREATE DATABASE if not exists School_DB")

        db = sql.connect(host="localhost", user="Ranvir", passwd="ranvir_sran", database="School_DB")
        mycursor = db.cursor()
        print(" Creating Student table")
        mycursor.execute("CREATE TABLE if not exists Students (AdmNo int primary key auto_increment, "
                         "StudentName varchar(30) not null, DOB date, Class char(3))")
        print(" Creating Employee table")
        mycursor.execute("CREATE TABLE if not exists Employees (EmpNo integer primary key auto_increment,"
                         "EmployeeName varchar(20),Job varchar(20),HireDate date)")
        print(" Creating Fee table")
        mycursor.execute("CREATE TABLE if not exists Fee (SrNo integer primary key auto_increment, "
                         "StudentName varchar(20), Fee char(5),Month varchar(15))")
        print(" Creating Exam table")
        mycursor.execute("CREATE TABLE if not exists exam (StudentName varchar(20),"
                         "SrNo integer primary key auto_increment, Obtained char(3), Total char(4))")
        print(" All tables created")

