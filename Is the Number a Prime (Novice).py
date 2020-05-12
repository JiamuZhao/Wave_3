from Function import prime_number


n = int(input("please give a positive integer number greater than one: "))
p = prime_number(n)
if p:
    print("This is a Prime Number")
else:
    print("This is not a Prime Number")
