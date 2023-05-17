def add(*values):
    
    sum = 0
    for i in values:
        sum += i
        
    print("Sum is ",sum)
    
def multi(*num):
    
    mul = 1
    for i in num:
        mul *= i
    print("Multiplication is ",mul)