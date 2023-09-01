#oops - says work with real world object, everything is object

#class - blueprint which is used for creating objects
#object - object world entity
#state and behaviour properties and functionality

class Laptop:

    def __init__(self,price,company):
        self.price = price
        self.company = company

    def myInfo(self):
        print("This is a ",self.company, " laptop and available for ",self.price)

obj = Laptop(50000,"Dell")
obj.myInfo()
obj1 = Laptop(75000,"HP")
obj1.myInfo()
