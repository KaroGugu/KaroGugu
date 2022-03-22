n = int(input())   # дължината на страна от площадката - квадрат
w = float(input()) # широчината на една плочка
l = float(input()) # дължината на една плочка
m = int(input())   # широчината на пейката
o = int(input())   # дължината на пейката

time_for_tile = 0.2 # Всяка плочка се поставя за 0.2 минути

area_squire = n * n
peika = m * o
area_for_tiles = area_squire - peika
tiles = w * l
area_for_tiles /= tiles
time = area_for_tiles * time_for_tile

print(round(area_for_tiles, 2))
print(round(time, 2))