car = {"Brand": "Ford",
       "Model":"Mustang",
       "Color": "Black Matt",
       "Year": 1998}
print(car)
x = car["Model"]
print(x)
print(car.get("Color"))
print(car.keys())
print(car.values())
print(car.items())
car["Year"] = 2000
print(car["Year"])
car.update({"Year" : 2012})
print(car["Year"])
