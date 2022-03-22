class Storage:
    storage = []  # class should also have an attribute - empty list, where all the items will be stored


    def __init__(self, capacity):  # should accept one parameter
        self.capacity = capacity

    def add_product(self, product: str):  # class should have two additional methods
        if self.capacity > 0:  # if there is enough space for it
            Storage.storage.append(product)   # adds the product in the storage
            self.capacity -= 1

    def get_products(self):  # returns the storage list
        return Storage.storage


# storage = Storage(4)  # storage = self, a 4 = capacity
# storage.add_product("apple")
# storage.add_product("banana")
# storage.add_product("potato")
# storage.add_product("tomato")
# storage.add_product("bread")
# print(storage.get_products())
