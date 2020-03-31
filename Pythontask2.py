from sys import exit
from random import randint

User_data = []
SN = 1  #User serial number variable
while True:
    firstname = input("Type in firstname: ")
    firstname_list = list(firstname)
    lastname = input("Type in lastname: ")
    lastname_list = list(lastname)
    email = input("Type in email: ")

    five_char = []  # list to contain the last five characters of password
    # to create a list of alphabets to contribute to the password
    alpha = "q w e r t y u i o p a s d f g h j k l z x c v b n m"
    alphabets = alpha.split()
    while len(five_char) != 5:
        five_char.append(randint(0, 9))
        if len(five_char) == 5:
            break
        five_char.append(alphabets[randint(0, 25)])

    # to convert each integer in the list to a string
    five_char = [str(char) for char in five_char]
    five_char = "".join(five_char)
    # join first two letters of the firstname
    f_pass = "".join(firstname_list[0:2])
    #  join last two letters of the lastname
    l_pass = "".join(lastname_list[-2:])

    password = f_pass + l_pass + five_char
    print(f"Your password is {password}")
    print("Do you want to create a new password?")

    while True:
        choice = input("Yes/No: ")
        if choice.lower() == "yes":
            password = input("Enter new password (7 characters): ")
            while len(password) < 7:
                print("Password must be at least 7 characters")
                password = input("Enter new password (7 characters): ")
            break
        elif choice.lower() == "no":
            break
        else:
            print("INVALID COMMAND! Type in Yes/No")

    user = {"Firstname": firstname,
            "Lastname": lastname,
            "Email": email,
            "Password": password}
    print(f"\nUser{SN} details: {user}\n")

    data = f"User{SN} details: {user}"
    User_data.append(data)  #store the new user data

    print("Do you want to enter another user?")
    while True:
        add_user = input("Yes/No: ")
        if add_user.lower() == "yes":
            print("")  #to print a blank line in the terminal
            SN += 1  #to add 1 to value of serial number variable(SN)
            break
        elif add_user.lower() == "no":
            print("\n", User_data)
            exit(0)
        else:
            print("INVALID COMMAND! Type Yes/No")
