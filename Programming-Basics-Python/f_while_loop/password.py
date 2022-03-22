user_name = input()
password = input()

data = input()                # парола за вход

while data != password:       # при въвеждане на грешна парола: потребителя да се подкани да въведе нова парола
    data = input()

print(f"Welcome {user_name}!")