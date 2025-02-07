# Calculate Simple Intrest

def simple_intrest(p: float|int, n: int, r:float|int) -> tuple:
    """
    p: Principle in INR
    n: Number of years
    r:Rate of intrest in percent per annum
    Output interst, amount
    """
    i = (p*n*r)/100
    a = p + i
    return i, a

# Take p, n, r as input from user
p = float(input("Please enter Principle in INR : "))
n = int(input("Please enter number of years : "))
r = float(input("Please enter rate of intrest in %p.a. : "))

# Call the simple intrest function
i, a = simple_intrest(p, n, r)

# Print the intrest and amount
print(f"Simple Intrest : {i:.2f} INR")
print(f"Amount : {a:.2f} INR")
