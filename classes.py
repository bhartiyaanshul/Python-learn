class person:
    name = "Anshul"
    occupation = "Developer"
    
    def info(self):
        print(f"{self.name} is a {self.occupation}")
        
        
a = person()
b = person()
c = person()

a.name = "Ridham"
a.occupation = "Full Stack Developer"

c.name = "Kashvi"
c.occupation = "Data Analyst"

a.info()
b.info()
c.info()