def prime_number(s):
    fac = []
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
