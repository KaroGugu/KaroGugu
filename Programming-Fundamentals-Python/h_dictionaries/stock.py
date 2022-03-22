elements = input().split()  # You will be given key-value pairs of products and quantities (separated by space)
searched_products = input().split()  # we read the products we have to search for and check for each of them
bakery = {}

for i in range(0, len(elements), 2):  # reading the products and adding them to the dictionary
    key = elements[i]
    value = elements[i + 1]
    bakery[key] = int(value)

# searched_product = input().split()  # we read the products we have to search for and check for each of them

for product in searched_products:
    if product in bakery:
        print(f"We have {bakery[product]} of {product} left")   # quantity of product left
    else:
        print(f"Sorry, we don't have {product}")

