u = "user1"
p = "pass1"

username = input("Enter Your Username: ")

if username == u:
    print("Your Username is Correct, Enter Your Password..")
    password = input("Enter Your Password: ")
    if password == p:
        print("You get the access of your account..")
    else:
        print("Your Password is Incorrect..")
else:
    print("Please Enter the correct username..")