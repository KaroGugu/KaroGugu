import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = '.,=+!?/@#$%&*()><{}'

all_combinations = lower + upper + numbers + symbols
length = 10
password = "".join(random.sample(all_combinations, length))
print(password)