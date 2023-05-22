class car:
    speed = 0
    color = ""
    type= ""
    def car_speed(self):
        self.speed = input("Enter a Car Speed: ")
        return self.speed
        
    def car_color(self):
        self.color = input("Enter a Car Color: ")
        return self.color
    
    def car_type(self):
        self.type = input("Enter a Car Type: ")
        
        
Tata = car()

Tata.car_type()
Tata.car_color()
Tata.car_speed()
print("Car Type:",Tata.type)
print("Car Color:",Tata.color)
print("Car Speed:",Tata.speed)
        

        