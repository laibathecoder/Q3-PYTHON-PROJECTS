# 18. **Property Decorators: @property, @setter, and @deleter**
# **Assignment:**  
# Create a class Product with a private attribute _price. 
# Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self):
        self._price = 0

    @property
    def price(self):
        print("Price is Getting...")
        return self._price

    @price.setter
    def price(self , value):
        self.value = value
        print("Price is Setting...")
        self._price = value
    
    @price.deleter
    def price(self):
        print("Price is deleting")
        self._price
    

p = Product()
p.price = 500
print(p.price)
del p.price


                         
