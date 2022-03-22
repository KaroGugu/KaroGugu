from math import ceil, floor

magnolii = int(input())
ziumbiuli = int(input())
rozi = int(input())
kaktusi = int(input())
podaruk = float(input())

poruchka = (magnolii * 3.25) + (ziumbiuli * 4) + (rozi * 3.50) + (kaktusi * 8)
taxes = poruchka * 5 / 100
pechalba = poruchka - taxes

difference = abs(podaruk - pechalba)

if pechalba >= podaruk:
    print(f"She is left with {floor(difference)} leva.")
else:
    print(f"She will have to borrow {ceil(difference)} leva.")
