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

# Encapsulation

1. We can set the data or the function as a private like (\_\_name) so it means name is private value. internally python represents these double underscore by using some name that's why we can't access them directly.
2. we can't access these private values or function directly
3. also we can use setter and getter method to access them
4. we can't get any values from setter method but we can get the values from getter method.

# Inheritance

1. Inherit all the variables and method from parent class to child class

# Method overriding

1. Override the parent method in child class and customize it
2. **str** convert refrence into an object
3. repr doing the same thing

# method overloading

1. method overloading means multiple methods can have same name with different parameters

int myMethod(int x)
float myMethod(float x)
double myMethod(double x, double y)

# static method and class method

1. static method call as @staticmethid and it will never send an object as first argument
2. class method will send a class refrence as a argument

# Polymorphism

1 . it means we have "many form" and it occurs when we have many clasees that are related to each other by inheritence

2.  Inheritance let's us inherit attributes and methods from another class. Polymorphism uses those methods to perform different tasks. This allows us to perform a single action in different ways.

# Abstraction

1. Data abstraction is the process of hiding certain details and showing only essential information to the user.

---> he abstract keyword is a non-access modifier, used for classes and methods:

2. Abstract class: is a restricted class that cannot be used to create objects (to access it, it must be inherited from another class).

3. Abstract method: can only be used in an abstract class, and it does not have a body. The body is provided by the subclass (inherited from).

# Interface

1. Another way to achieve abstraction is with interfaces.

An interface is a completely "abstract class" that is used to group related methods with empty bodies:

----->>>>>>>>>> Like abstract classes, interfaces cannot be used to create objects (in the example above, it is not possible to create an "Animal" object in the MyMainClass)
Interface methods do not have a body - the body is provided by the "implement" class
On implementation of an interface, you must override all of its methods
Interface methods are by default abstract and public.

---

Why And When To Use Interfaces?

1. To achieve security - hide certain details and only show the important details of an object (interface).
