class Item:
    pay_rate = 0.9  # class attribute

    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_item(self):
        return self.price*self.quantity

    def summary(self):
        return f"Name:{self.name}"

    # represent object as it is
    def __repr__(self):
        pass

    # from this decorator we can use decorator to say this classmethod
    # this cls will represent the class instead of instance
    @classmethod
    def instantiate_from_csv(cls):
        pass


Item.instantiate_from_csv()
item1 = Item("John", 100)

# item1.name = "John"

# item1.quantity = 5
# item1.price = 100

print(item1.calculate_item())
print(item1.summary())

# second instance

item2 = Item("john cw", 1001, 51)
item2.hasNumPad = False
# item2.name = "John cw"

# item2.quantity = 51
# item2.price = 1001

print(item2.calculate_item())
print(item1.name + ' ' + item2.name)
print(item2.hasNumPad)

print(Item.pay_rate)


class Student(Item):
    def __init__(self, name, price, quantity, email):
        super().__init__(name, price, quantity)
        self.email = email

    # method override
    def summary(self):
        return f"Name:{self.name} price:{self.price} Email:{self.email}"

    # _str_
    def __str__(self):
        return f"Name:{self.name} price:{self.price} Email:{self.email}"
    # repr doing the same as str

    def __repr__(self):
        return f"Name:{self.name} price:{self.price} Email:{self.email}"


s1 = Student("Farshid", 100, 11, "arnob.farshid@gmail.com")
s2 = Student("Farshid", 100, 11, "arnob22.farshid@gmail.com")
print(s1.summary())
print(s1)
print(s2)
