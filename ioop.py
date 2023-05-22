class account:
    
    def __init__(self,user_name,password,name,phone):
        self.user_name = user_name 
        self.pass_word = password
        self.name = name
        self.phone = phone
        
        self.loggedin = False
        
    def login(self):
        self.username = input("Enter Your Username: ")
        self.password = input("Enter Your Password: ")
        if self.username == self.user_name:
            if self.password == self.pass_word:
                print("Logged In..")
                self.loggedin = True
            else:
                print("Enter a Correct Password..")
        else:
            print("Enter a Correct Username..")
            
    def info(self):
        if self.loggedin == True:
            print("Your Name is {} and Phone Number is {}".format(self.name,self.phone))
        else:
            print("Please Login First..")
            
    def logout(self):
        if self.loggedin == True:
            self.loggedin == False
            print("You Are Logged Out..")
        else:
            print("You Are Already Logged Out..")
            
            
user1 = account("Anshul","ansh@5339","Anshul",7043163805)
user1.login()
user1.info()
user1.logout()
           