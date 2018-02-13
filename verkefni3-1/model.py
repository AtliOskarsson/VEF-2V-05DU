import sqlite3, sys

def login():
    while True:
        username = input("Enter Username: ")
        password = input("Enter Password :")
        with sqlite3.connect("Qui.db") as db:
            cursor = db.cursor()

        find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
        cursor.execute(find_user, [(username), (password)])
        results = cursor.fetchall()

        if results:
            for x in results:
                print("Welcome " + x[2])
            break
            #return("Exit")

        else:
            print("Username or password not recognized")
            again = input("Do you want to try again?(y/n): ")
            if again.lower() == "n":
                print("Goodbye.")
                #return("Exit.")
                break


def signup():
    found = 0
    while found == 0:
        username = input("Enter a usernam: ")
        with sqlite3.connect("Qui.db") as db:
            cursor = db.cursor()

        findUser = ("SELECT * FROM user WHERE username = ?")
        cursor.execute(findUser, [(username)])

        if cursor.fetchall():
            print("Username taken.")

        else:
            found = 1

    firstname = input("Firstname: ")
    surname = input("Surname: ")
    password = input("Password: ")
    passwordAgain = input("Reenter Password: ")
    while password != passwordAgain:
        print("The password did not match the verification password")
        password = input("Password: ")
        passwordAgain = input("Reenter Password: ")
    insertdata = """INSERT INTO user(username,firstname,surname,password) 
    VALUES(?,?,?,?);"""

    cursor.execute(insertdata, [(username), (firstname), (surname), (password)])
    db.commit()

def menu():
    print("WELCOMMME!!!!!!")
    while True:
        menu = ("""
        1 - Create New User
        2 - Login
        3 - Exit\n
        >> """)

        userChoice = input(menu)

        if userChoice == "1":
            signup()

        elif userChoice == "2":
            login()

        elif userChoice == "3":
            print("Cunt")
            sys.exit()

        else:
            print("Invalid input")


menu()