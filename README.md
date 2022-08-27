# Object oriented Programming

Example with codes and notes:
class Item:
def **init**(self):
print("I am created")
def calculate_total_price(self,x,y):
return x\y

# class is the blueprint -->human is the bluprint

# Object what we are seeing ->> from this blueprint we create different types of humans

# when you called a def inside a class it is called method and when its called outside class it is called function

# we have to called self inside a class method as its argument because it refers to the object and outside the we can call without argument.

# if we do not use self inside a class method then it will cause an error.

# We can declare properties in constructor and it is called by **init**

# when we create an instance of a class the constructor run automatically at the first.

# we can pass all the properties as an argument of a constructor

# we can also pass default value to am argument if we dont know what is the exact amount will be

# we can add more argunets without passing the init methods

# we define the types of the properties like we can declare name must be string type

    ->>>>>>>> Example :name:string

    --------> We can add assert to check the validation of our argument and it is easy fixed the bug

->>>>Example: 1. def **init**(self, name, price, quantity):
self.name = name ->>>self.name means refering an particular instance of a class.
self.price = price
self.quantity = quantity

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

# There are another type of attribute and we can call it class attribute

# when you cant find attribute from an instance we can go to the class attribute

# repr represent the exact version of the object used to be.

# decorator is the quick way to change behaviour of the function.It is calling them just before the function

# in this example it is called the classmethod inside this this cls will represent the class.

->>>>Example::

@classmethod
def instantiate_from_csv(cls):
pass
print(item1.calculate_item())
