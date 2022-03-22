import math
from math import pi
radians = float(input())

degrees = radians * 180 / pi
print(math.floor(degrees))    # math.floor(…) – закръглянето да е винаги надолу, закръгля до цяло число