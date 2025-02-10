def simple_intrest(p,n,r):
    i = (p*n*r)/100
    a = p + i
    return i, a

p = int(input("enter Principle in INR : "))
n = float(input("enter numbet of years : "))
r = float(input("enter rate of intrest : "))

i, a = simple_intrest(p, n, r)

print(f"Simple intrest ={i:.2f} INR")
print(f"Amount = {a:.2f} INR")