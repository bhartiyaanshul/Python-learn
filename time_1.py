import time
timelab = time.strftime('%H : %M : %S')
timelab2= int(time.strftime('%H'))
print(timelab)
if timelab2 >= 5 and timelab2 <12:
    print("Good Morning Sir...")
elif timelab2 >= 12 and timelab2 < 17:
    print("Good After Noon Sir...")
elif timelab2 >= 17 and timelab2 <20:
    print("Good Evening Sir...")
else :
    print("Good Night Sir...")
