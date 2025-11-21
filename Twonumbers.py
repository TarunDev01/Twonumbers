import sys
if len(sys.argv) != 3:
    print("Usage: python Twonumber.py <num1> <num2>")
    sys.exit()
else
    num1=20
    num2=30
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])

if num1 > num2:
    print(num1, "is greater")
elif num2 > num1:
    print(num2, "is greater")
else:
    print("Both numbers are equal")
