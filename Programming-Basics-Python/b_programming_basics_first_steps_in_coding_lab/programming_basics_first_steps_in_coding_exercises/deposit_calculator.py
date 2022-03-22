deposit = float(input())

months = int(input())

annual_interest_percent = float(input())

# годишен лихвен процент = депозит * % от годишната лихва
annual_interest_percent = deposit * annual_interest_percent / 100
# да намеря месечната лихва
monthly_interest = annual_interest_percent / 12

# да пресметна крайната сума, в края на периода = депосит + лихвата за дадения периода
total_sum = deposit + (months * monthly_interest)

print(total_sum)