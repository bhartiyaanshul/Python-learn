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
while (True):
    s = input("Enter Number for Following service \n1) Deposite \n2) Withdraw \n3) Balance: \n4) Exit ATM\n")
    if 1 <= int(s) <= 4:
            if s == 1:
                if s >= 0 and s <= 9:
                    deposit = int(input("Enter a amount to be deposit in your account: "))
                    balance += deposit
                    print("Your Balance after deposit is ", balance)
                else:
                    print("Enter a Valid Amount")
            
            elif s == 2:
                withdraw = int(input("Enter a amount you have to withdraw: "))
                balance -= withdraw
                print("Your Balance after withdraw is ", balance)

            elif s == 3:
                print("Your Balance is ", balance)
                
            else:
                print("You Have Exited the ATM Machine, Thank You")
                break
    else:
        print("Enter a Valid Option..")
        
        
    

