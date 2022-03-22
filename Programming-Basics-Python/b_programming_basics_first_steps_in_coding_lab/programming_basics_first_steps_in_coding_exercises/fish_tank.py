length = int(input())
width = int(input())
height = int(input())
percent_sand = float(input())

all_volum = length * width * height / 1000    # ние търсим литри, a 1 л = 1 дм3
                                          # затова превръщаме от см3 в дм3 , a 1см = 10 дм
                                          # 1дм3 = 10см * 10см * 10см

percent_sand = all_volum * percent_sand / 100  # за да превърнем цялото число в %
water_valum = all_volum - percent_sand
print(water_valum)