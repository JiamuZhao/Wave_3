fac = []


def prime_number(s):
    if s >= 2:
        for t in range(2, s):
            if s % t == 0:
                fac.append(t)
    else:
        return False

    if s >= 2:
        if len(fac) > 1:
            return False
        else:
            return True


n = int(input("please give a positive integer number greater than one: "))
p = prime_number(n)
if p:
    print("This is a Prime Number")
else:
    print("This is not a Prime Number")