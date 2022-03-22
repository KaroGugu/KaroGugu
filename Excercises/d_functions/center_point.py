from math import floor


# centered at the origin of the plane, may be described as the set of all points
# whose coordinates x and y satisfy the equation x2 + y2

def closest_point_to_center(x_1, y_1, x_2, y_2):
    if x_1 ** 2 + y_1 ** 2 <= x_2 ** 2 + y_2 ** 2:
        return f"{floor(x_1), floor(y_1)}"
    else:
        return f"{floor(x_2), floor(y_2)}"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(closest_point_to_center(x1, y1, x2, y2))
