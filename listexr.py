# n = int(input("Enter Limit: "))

# even = []
# odd = []

# for i in range(1,n+1):
#     a = int(input("Enter Number: "))
#     if a % 2 == 0:
#         even.append(a)
#     else:
#         odd.append(a)
        
        
# print("Even Number are ",even)
# print("Odd Numbers are ",odd)

# n = int(input("Enter a Number: "))

# ans = []

# for i in range(2,n):
#     if n % i == 0:
#         ans.append(i)
        
        
# print(f"{n} is divisible by",ans)

n = int(input("Enter Limit: "))

list1 = []
even = []
odd = []

for i in range(1,n+1):
    a = int(input("Enter Number: "))
    list1.append(a)
    if a % 2 == 0:
        even.append(a)
    else:
        odd.append(a)
        
print("List",list1)    
print("Even Number are ",even)
print("Odd Numbers are ",odd)
print("Sum of even number is",sum(even))
print("Sum of Odd number is",sum(odd))

