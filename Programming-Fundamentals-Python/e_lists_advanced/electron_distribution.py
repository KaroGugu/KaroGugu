number_of_electrons = int(input())
shell_list = []

for each_layer in range(1, number_of_electrons + 1):
    shell = 2 * each_layer ** 2
    if number_of_electrons >= shell:
        shell_list.append(shell)
        number_of_electrons -= shell

    else:
        shell_list.append(number_of_electrons)
        each_layer = 0
        break

print(shell_list)