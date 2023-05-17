# def food(food):
#     for x in food:
#         print(x)
        
# fastfood = ["Burger","Pizza","French Fries"]
# food(fastfood)


# def multi(x):
#     return x * 5

# print(multi(5))


# def lenght(list1):
#     i = 0
#     for items in list1:
#         i+=1
        
#     return (i)
    
# list2 = "anshul"
# ans = lenght(list2)
# print(ans)

# def sum(num):
#     sum = 0
#     for i in num:
#         sum += i
#     return (sum)

# def min(num):
#     min = num[0]
#     for i in num:
#         if i < min:
#             min = i
            
#     return (min)

# def max(num):
#     max = num[0]
#     for i in num:
#         if i > max:
#             max = i
            
#     return (max)

# var = []
# r = int(input("Enter the range of list: "))
# for i in range(r):
#     a = int(input("Enter Numbers : "))
#     var.append(a)
    
    
# print(sum(var))
# print(min(var))
# print(max(var))


def sum(*values):
    sum = 0
    for i in values:
        sum += i
    return (sum)     

print(sum(1,23,4,5,67,88))


        