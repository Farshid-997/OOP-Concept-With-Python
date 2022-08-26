# Object oriented Programming

Example with codes and notes:
class Item:
def **init**(self):
print("I am created")
def calculate_total_price(self,x,y):
return x\y

# when you called a def inside a class it is called method and when its called outside class it is called function

# we have to called self inside a class method as its argument because it refers to the object and outside the we can call without argument.

# if we do not use self inside a class method then it will cause an error.

# We can declare properties in constructor and it is called by **init**

# when we create an object of a class the constructor run automatically at the first.

->>> When we first created an instance it will called the constructor then execute it after 2nd time for the instacne it will call again.

item1=Item()
item1.name="John"

item1.quantity=5
item.price=100
item1.calculate_total_price(item1.price,item1.quantity)

# here name,quantity and price are called attribute

#we can create another object

item2=Item()

print(type(item1))#item type
print(type(item1))#str type
print(type(item1))#int type
print(type(item1))#int type
