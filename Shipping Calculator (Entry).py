def shipping_calculator(s):
    if s > 0:
        if s == 1:
            a = 10.95
        else:
            a = '%.2f' % (2.95 * (s - 1) + 10.95)
        return a
    else:
        return "Invalid Value"


p = int(input("please enter the number of cargo: "))
m = shipping_calculator(p)
if p > 0:
    print(f"Your Shipping Charge is ${m}")
else:
    print(f"Your Shipping Charge is {m}")
