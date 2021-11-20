# Import Math
import math

# Greet
print("I can calculate a/b + c/d where a,b,c and d are integers.")

# Input Loop
validInput = False
while validInput == False:
    try:
        a = int(input("a:"))
        b = int(input("b:"))
        c = int(input("c:"))
        d = int(input("d:"))
        if b != 0 and d != 0:
            print("Thank you, I will add these fractions now")
            validInput = True
        elif b==0 or d==0:
            print("Denominators cannot be zero.")
    except:
        print("That is not a number!")

# Calculate answer
top = a*d + b*c
bottom = b*d
gcd = math.gcd(top,bottom)

# Divide out common term
top /= gcd
bottom /= gcd

# Put the minus on the top
if bottom < 0:
    top *= -1
    bottom *= -1

# Make the numbers ints
top = int(top)
bottom = int(bottom)

# The answer message
message = "Answer is "+str(top)+"/"+str(bottom)
message = message.replace("/1","")
print(message)
print("The decimal answer would be", round(top/bottom,4),"to 4 dp.")

# quit
quit()