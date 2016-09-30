def clip(lo, x, hi):
    return min(max(lo, x), hi)

low_number = float(input("enter 1st valid number as float: "))
high_number = float(input("enter 2nd valid number as float (2nd number > 1st number): "))
number = float(input("enter any valid float number: "))
print(clip(low_number, number, high_number))

