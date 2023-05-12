n = int(input("Enter a range"))
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(i+1,end="")
        
    
#     print("\r")

# for i in range(0,n):
#     for j in range(0,i+1):
#         print(j+1,end="")
        
        
#     print("\r")

# temp =1
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(temp,end="")
#         temp += 1
        
    
#     print("\r")

# for i in range(1,n):
#     for j in range(i,0,-1):
#         print(j,end="")
        
    
#     print("\r")

# for i in range(1,n):
#     num = 1
#     for j in range (n,0,-1):
#         if j > i:
#             print(" ",end="")
#         else:
#             print(num,end="")
#             num += 1
            
#     print("\r")
    
# for i in range(0,n):
#     for j in range (n-i,0,-1):
#         print(j,end="")
            
#     print("\r")


# for i in range(n):
#     print(" " * i,end="")
#     for j in range (i+1,n+1):
#         print(j,end="")
            
#     print("\r")

# for i in range(n,0,-1):
#     for j in range(i-1,0,-1):
#         print(i,end="")
    
#     print("\r")
for i in range(0,n):
    for j in range(n,0,-1):
        if j>i:
            print(" ",end="")
        else:
            print(j,end="")
    
    print("\r")    