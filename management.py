import mysql.connector as sql
from db_layout_data import data_dict


class Management:
    def __init__(self, choice):
        """ RUNS WHEN THE OBJECT IS CREATED. SOME PRE-REQUISITE CONSTANTS ARE CREATED FOR LATER USE
            AND NEXT STEP IS CHOSEN """
        db = sql.connect(host="localhost", user="localhost", passwd="123456", database="School_DB")
        self.actions = data_dict[choice]["Options"]
        self.queries = data_dict[choice]["Respective Queries"]
        self.db_name = data_dict[choice]['DB_Name']

        # PROMPT FOR NEXT STEP
        print(f"\n\nWelcome to {choice} system")
        for action in self.actions:
            print(action)
        self.index = int(input(f"\nEnter your choice(1-{len(self.actions)}): "))

        # RUNNING THE REQUIRED FUNCTION
        self.action_chosen = self.op_dict[self.index]
        self.action_chosen(self, choice)

    def add(self, choice):
        db = sql.connect(host="localhost", user="localhost", passwd="123456", database="School_DB")
        mycursor = db.cursor()
        data_to_add = tuple()

        try:
            # APPENDING DATA TO ADD LATER
            for i in range(3):
                query = input(f"{self.queries[i]}: ")
                data_to_add += (query,)
        except ValueError:
            # RE-RUNNING THE FUNCTION
            print("Incorrect Inputs, Please Try Again")
            self.add(choice)

        ID = 0
        try:
            # ADDING ONE FIELD DATA IN AN ENTRY AND THEN EDITING AND ADDING OTHER DETAILS
            for i in range(3):
                    if ID == 0:
                        mycursor.execute(f"insert into {self.db_name}({data_dict[choice]['DB_Fields'][i+1]})"
                                         f" values('{data_to_add[i]}')")
                        db.commit()
                        mycursor.execute(f"Select {data_dict[choice]['DB_Fields'][0]} from {data_dict[choice]['DB_Name']}")
                        temp_list = mycursor.fetchall()
                        ID = temp_list[-1][0]
                    else:
                        mycursor.execute(f"update {self.db_name} set {data_dict[choice]['DB_Fields'][i+1]} = "
                                         f" '{data_to_add[i]}' where {data_dict[choice]['DB_Fields'][0]} = {ID}")
                        db.commit()
        except:
            print("We have encountered an unexpected error, please try again later....")
            return
        else:
            print("New Data has been uploaded successfully")

    def update(self, choice):
        try:
            # RETRIEVING ALREADY EXISTING IDS
            db = sql.connect(host="localhost", user="localhost", passwd="123456", database="School_DB")
            mycursor = db.cursor()
            id_ = int(input(f"{data_dict[choice]['DB_Fields'][0]}: "))
            mycursor.execute(f"select {data_dict[choice]['DB_Fields'][0]} from {data_dict[choice]['DB_Name']}")
            record = mycursor.fetchall()
        except:
            print("Unable to Retrieve Data, Try Again later")
            return

        # STORING IDS IN A LIST TO COMPARE AGAINST
        id_tuple = []
        for entry in record:
            id_tuple.append(entry[0])

        # CHECKING IF ID EXISTS AND THEN UPDATING DATA
        if id_ in id_tuple:
            entry = input(f"Update {data_dict[choice]['Respective Queries'][2]} to: ")
            mycursor.execute(f"update {data_dict[choice]['DB_Name']} "
                             f"set {data_dict[choice]['DB_Fields'][3]} = '{entry}' "
                             f"where {data_dict[choice]['DB_Fields'][0]} = {id_}")
            db.commit()
            print("Record has been updated.")
        else:
            # RECURSION
            print("Record does not exist, please enter an existing id.")
            self.update(choice)

    def remove(self, choice):

        try:
            # RETRIEVING ALREADY EXISTING IDS
            db = sql.connect(host="localhost", user="localhost", passwd="123456", database="School_DB")
            mycursor = db.cursor()
            id_ = int(input(f"{data_dict[choice]['DB_Fields'][0]}: "))
            mycursor.execute(f"select {data_dict[choice]['DB_Fields'][0]} from {data_dict[choice]['DB_Name']}")
            record = mycursor.fetchall()
        except:
            print("Unable to Retrieve Data, Try Again later")
            return

        # STORING IDS IN A LIST TO COMPARE AGAINST
        id_tuple = []
        for entry in record:
            id_tuple.append(entry[0])

        # CHECKING IF ID EXISTS AND THEN DELETING DATA
        if id_ in id_tuple:
            mycursor.execute(f"delete from {data_dict[choice]['DB_Name']} where "
                             f"{data_dict[choice]['DB_Fields'][0]} = {id_}")
            db.commit()
            print("Data has been deleted")
        else:
            # RECURSION
            print("AdmNo. does not exist, try again.")
            self.remove(choice)

    def display(self, choice):
        try:
            # RETRIEVING DB DATA
            db = sql.connect(host="localhost", user="localhost", passwd="123456", database="School_DB")
            mycursor = db.cursor()
            mycursor.execute(f"Select * from {data_dict[choice]['DB_Name']}")
        except:
            print("Can't retrieve data, try again later...")
            return

        # PRINTING IT
        data = mycursor.fetchall()
        for entry in data:
            for i in range(4):
                print(f"{data_dict[choice]['DB_Fields'][i]}: {entry[i]}")
            print("\n")

    # The choice made in the start retrieves a value from here and then the corresponding function is ran
    op_dict = {
        1: add,
        2: update,
        3: remove,
        4: display
    }
