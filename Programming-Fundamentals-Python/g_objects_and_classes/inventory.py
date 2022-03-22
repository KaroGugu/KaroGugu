class Inventory:

    def __init__(self, capacity: int):
        # The __init__ method should accept only the __capacity: int (private attribute) of the inventory
        self.__capacity = capacity
        self.items = []
        # Each inventory should also have an attribute called items - empty list, where all the items will be stored

    def add_item(self, item: str):  # adds the item in the inventory if there is space for it
        if self.__capacity > len(self.items):
            self.items.append(item)
        else:
            return "not enough room in the inventory"

    def get_capacity(self):  # returns the value of __capacity
        return self.__capacity

    def __repr__(self):
        current_capacity = len(self.items) - self.__capacity
        return f"Items: {', '.join(self.items)}.\nCapacity left: {current_capacity}"



inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
