print("Something happening")
print("I love u guys")
print("something")

class Car:
    #private String brand
    def __init__(self, brand):
        self.brand = brand 
    def get_brand(self):
        return self.brand


car1 = Car("pandy")
print(car1.get_brand) 