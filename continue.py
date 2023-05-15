# for n in range(1,11):
#     if n == 3 or n == 7:
#         continue
#     print(n)


n = int(input("Enter a range:"))

for i in range(1,n+1):
    if i % 2 == 0:
        continue
    else:
        print(i)