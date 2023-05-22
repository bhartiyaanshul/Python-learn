balance = 0

# s = int(input("Enter Number for Following service \n1) Deposite \n2) Withdraw \n3) Balance: \n"))

# match s:
#     case 1:
#         deposit = int(input("Enter a amount to be deposit in your account: "))
#         balance += deposit
#         print("Your Balance after deposit is ",balance)


#     case 2:
#         withdraw = int(input("Enter a amount you have to withdraw: "))
#         balance -= withdraw
#         print("Your Balance after withdraw is ",balance)
#     case 3:
#         print("Your Balance is ",balance)
try:
    
    while (True):
            s = int(input("Enter Number for Following service \n1) Deposite \n2) Withdraw \n3) Balance: \n4) Exit ATM\n"))
            try:
                if s == 1:
                    deposit = int(input("Enter a amount to be deposit in your account: "))
                    balance += deposit
                    print("Your Balance after deposit is ", balance)
            
                elif s == 2:
                    withdraw = int(input("Enter a amount you have to withdraw: "))
                    balance -= withdraw
                    print("Your Balance after withdraw is ", balance)

                elif s == 3:
                    print("Your Balance is ", balance)
                            
                else:
                    print("You Have Exited the ATM Machine, Thank You")
                    break
            except:
                print("Please Enter Numeric Value..")
except:
    print("Please select from the following option..")    

        
        
    

