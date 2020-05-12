import math


def cal_hypotenuse(a, b):
    if a > 0 and b > 0:
        return math.sqrt(a ** 2 + b ** 2)
    else:
        return "Invalid Value"


p = int(input("Please enter the length of first shorter side: "))
q = int(input("Please enter the length of second shorter side: "))
cal_hypotenuse(p, q)
print(f"The hypotenuse of the triangle is {cal_hypotenuse(p, q)}")