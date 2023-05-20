i = input("Enter Your Input: ")
num = 0
char = 0
special = 0
for items in i:
    if items.isdigit():
        num += 1
    elif items.isalpha():
        char += 1
    else:
        special += 1
        
print("Numbers : ",num)
print("Characters: ",char)
print("Special Characters: ",special)
    