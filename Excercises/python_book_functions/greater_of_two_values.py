input_type = input()
value_1 = input()
value_2 = input()

def get_greater_value(input_t, v_1, v_2):
    result = None
    if input_t == "int":
        if int(v_1) > int(v_2):
            result = v_1
        elif input_t(v_1) < int(v_2):
            result = v_2
        else:
            result = v_1

    elif input_t == "char":
        if ord(v_1) > ord(v_2):
            result = v_1
        elif ord(v_1) < ord(v_2):
            result = v_2
        else:
            result = v_1

    else:
        if v_1 > v_2:
            result = v_1
        elif v_1 < v_2:
            result = v_2
        else:
            result = v_1

    return result

print(get_greater_value(input_type, value_1, value_2))