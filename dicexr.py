para = input("Enter a paragraph: ")

words = para.split()

counter = {}

for word in words:
    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1
        
        
print(counter)