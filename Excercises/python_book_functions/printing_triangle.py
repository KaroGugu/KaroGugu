n = int(input())

def print_line(num):
    for i in range(1, num + 1):  # number of rows
        for j in range(1, i + 1):         # number of symbols per row
            print(f"{j} ", end="")    # stay on the same row

        print()

    for i in range(num - 1, 0, -1): # number of rows backward
        for j in range(1, i + 1):   # # number of symbols per row
            print(f"{j} ", end="")  # stay on the same row

        print ()

print_line(n)