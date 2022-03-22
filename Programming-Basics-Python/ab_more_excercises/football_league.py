import string

stadium_capacity = int(input())
fens = int(input())

fen_a = 0
fen_b = 0
fen_v = 0
fen_g = 0

for fen in range(fens):
    sector = input()
    if sector in string.ascii_letters:
        if sector == "A":
            fen_a += 1
        elif sector == "B":
            fen_b += 1
        elif sector == "V":
            fen_v += 1
        elif sector == "G":
            fen_g += 1
percent_a = fen_a / fens * 100
percent_b = fen_b / fens * 100
percent_v = fen_v / fens * 100
percent_g = fen_g / fens * 100

percent_all_fens = fens / stadium_capacity * 100

print(f"{percent_a:.2f}%")
print(f"{percent_b:.2f}%")
print(f"{percent_v:.2f}%")
print(f"{percent_g:.2f}%")
print(f"{percent_all_fens:.2f}%")