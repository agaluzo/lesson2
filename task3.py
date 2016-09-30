from math import pi, tan


def polysum(n, s):
    area = 0.25 * n * s**2 / tan(pi/n)
    square_length = (n*s)**2
    return round(area + square_length, 4)

sides_number = int(input("enter number of sides as int: "))
side_length = int(input("enter length as int: "))
print(polysum(sides_number,side_length))
