# Simple arithmetic progression calculator
##
# Finding the nth term of a progression given the first,second and third term
##

print("Simple Arithmetic progression calculator")
# (declare all variables)
print("what term are we looking for? Sum of series(s) or nth term(n)")
choose = input("??: ")
a = int(input("Input first term(a): "))
t2 = int(input("Input second term(t2): "))
t3 = int(input("Input third term(t3): "))
c = int(input("Input nth term: "))
d = t3 - t2
# c is the nth term we're looking for
nth = a + (c - 1) * d
sum = (c / 2) * (2*a + (c-1) * d)
# (end declaration)
if choose == "n":
    print("Let's find the " + str(nth) + "th" + " term of a series")
    print("The " + str(nth) + "th" + " term of the series " + str(a) + ", " + str(t2) + " and " + str(t3) + " is " + str(nth) +" in the sequence "+ str(nth)+ " " + str(nth + d) + " " + str(nth +( 2 * d)) + ".......")
    ######
elif choose == "s":
              print("Let's find the sum of a series to the" str(nth) + "number")
              print("The sum of the progression of the series " + str(a) + ", " + str(t2) + "," + str(t3) +" and " + str(nth)+ " is " + str(sum))
else:
    print("select a valid option please")
######