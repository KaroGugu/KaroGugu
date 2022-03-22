def tribonacci(start,num):
    if num >= 3:                  # every number is formed by the sum of the previous 3
        for i in range(num - 1):
            num = sum(start[-3:])
            start.append(num)
        return start

    else:
        for i in range(num - 1):
            num = sum(start[-2:])
            start.append(num)
        return start

start = [1]

number = int(input())
print(*tribonacci(start, number))