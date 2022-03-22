from math import trunc

v_pool = int(input())
p1_debit = int(input())
p2_debit = int(input())
time = float(input())

# Обем напълнен от тръбите
v_p1 = p1_debit * time
v_p2 = p2_debit * time
total_pipes_volume = v_p1 + v_p2

# Процент за всяка тръба
v_p1_percent = v_p1 / total_pipes_volume * 100
v_p2_percent = v_p2 / total_pipes_volume * 100

# Процент запълненост на басейна и преливане
v_pool_percent = total_pipes_volume / v_pool * 100
overflow = total_pipes_volume - v_pool

if total_pipes_volume > v_pool:
    print(f"For {time} hours the pool overflows with {trunc(overflow)} liters.")
else:
    print(f"The pool is {trunc(v_pool_percent)}% full. Pipe 1: {trunc(v_p1_percent)}%. Pipe 2: {trunc(v_p2_percent)}%.")