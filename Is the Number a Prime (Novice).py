s = int(input("please give a positive integer number greater than one: "))

fac = []
if s >= 2:
    for t in range(2, s):
        if s % t == 0:
            fac.append(t)
else:
    print("Invalid Number")

if s >= 2:
    if len(fac) > 1:
        print("False")
    else:
        print("True")
