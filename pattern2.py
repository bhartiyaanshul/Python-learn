# n = int(input("Enter the lenght:"))
# i = 1
# while(i<=n):
#     j = 1
#     while(j<=i):
#         print("*",end=" ")
#         j += 1
#     print()
#     i += 1

# i = 5
# while(i<=n):
#     j = 5
#     while(j<=i):
#         print("*",end=" ")
#         j += 1
        
#         print()
#         i += 1

# for i in range(n):
#     print(" "*(n-i-1)+"* "*(i+1))
# for j in range(n-1,0,-1):
#     print(" "*(n-j)+"* "*(j))


# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#         print("*",end=" ")
       
#     print()


# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ") 
        
#     print()       
# for i in range(n-1):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")
    
        
#     print()

rows = 7
cols = 7

for row in range(11):
    for col in range(11):
        if (col == 0 and row < 5 ) or (col == 5) or (row == 5 and col != 5) or (row == 0 and col >=6) or (row > 5 and col == 10) or (row == 10 and col<5) or (col==2 and row == 2) or (col==8 and row== 2) or (col==2 and row== 7) or (col==8 and row== 7):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        
    print()