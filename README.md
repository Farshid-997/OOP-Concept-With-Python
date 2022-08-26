Object oriented Programming

class Item:
def calculate_total_price(self):

#when you called a def inside a class it is called method and when its called outside class it is called function
#we have to called self inside a class method as its argument because it refers to the object and outside the we can call without argument.

# if we do not use self inside a class method then it will cause an error.

item1=Item()
item1.name="John"

item1.quantity=5
item.price=100

#here name,quantity and price are called attribute

#we can create another object

item2=Item()

print(type(item1))#item type
print(type(item1))#str type
print(type(item1))#int type
print(type(item1))#int type
