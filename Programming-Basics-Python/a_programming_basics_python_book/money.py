bitcoin = int(input())
ioan = float(input())
commission = float(input()) / 100

# 1 биткойн = 1168 лева
# 1 китайски юан = 0.15 долара
# 1 долар = 1.76 лева
# 1 евро = 1.95 лева
dolar = 0

bitcoin_to_lev = bitcoin * 1168
ioan_to_dolar = ioan * 0.15
dolar_to_lev = ioan_to_dolar * 1.76

# euro = 1.95

money_in_lv = bitcoin_to_lev + dolar_to_lev
money_in_euro = money_in_lv / 1.95
commission *= money_in_euro
total_sum = money_in_euro - commission

print(f'{total_sum:.2f}')