import re

numbers_of_iteration = int(input())

for i in range(numbers_of_iteration):
    data = input()
    pattern = r'(\@\#+)([A-Z][a-zA-Z0-9]+[A-Z])(\@\#+)'
    result = re.match(pattern, data)

    if result is None or len(result.group()) < 10: # surrounded by a "@" followed by one or more "#" + 6 characters long
        print("Invalid barcode")
    else:  #  product group is obtained by concatenating all the digits found in the barcode
        extract_nums = re.findall(r"\d", result.group())

        if not extract_nums:  # If there are no digits present in the barcode
            print("Product group: 00")
        else:
            print(f"Product group: {''.join(extract_nums)}")
