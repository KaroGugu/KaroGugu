base = float(input())
height = float(input())

def area_of_triangle(b, h):
    area = b * h / 2
    return area

result = area_of_triangle(base, height)

print(f"{result:.12g}")