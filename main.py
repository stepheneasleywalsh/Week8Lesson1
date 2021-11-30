import math # import math

# Ask the user for a b c and d
print("I will calculate a/b + c/d")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))

# Check that you are not dividing by 0
if b == 0 or d == 0:
    print("Sorry, can't do that!!!!!")
    quit()

# Calculates the answer simplifed
numerator = a*d + b*c
denominator = b*d
GCD = math.gcd(numerator,denominator)
numerator /= GCD
denominator /= GCD

# Checks if the denominator is negative
if denominator < 0:
    denominator *= -1
    numerator *= -1

# Checks if the denominator is 1 then prints the answer with the question
if denominator == 1:
    print(a,"/",b,"  plus  ",c,"/",d,"   is   ",int(numerator))
else:
    print(a,"/",b,"  plus  ",c,"/",d,"   is   ",int(numerator),"/",int(denominator))

# quit
quit()