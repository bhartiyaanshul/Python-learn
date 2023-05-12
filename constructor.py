class person:
    def __init__(self,name,occ):
        self.name = name
        self.occ = occ
        
    def info(self):
        print(f"{self.name} is {self.occ}")

a = person("Anshul","Developer")
b = person("Ridham","Developer")
c = person("Kashvi","Data Analyst")
a.info() 
b.info()
c.info()     