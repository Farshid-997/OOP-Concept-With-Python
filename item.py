class Item:
    def __init__(self):
        print("I am created")

    def calculate_item(self, x, y):
        return x*y


item1 = Item()
item1.name = "John"

item1.quantity = 5
item1.price = 100

print(item1.calculate_item(item1.price, item1.quantity))


# second instance

item2 = Item()
item2.name = "John cw"

item2.quantity = 51
item2.price = 1001

print(item2.calculate_item(item2.price, item2.quantity))
