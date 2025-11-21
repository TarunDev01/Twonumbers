import sys

# Check if two arguments are provided
if len(sys.argv) != 3:
    print("Usage: python program.py <num1> <num2>")
    sys.exit()

# Convert command-line arguments to numbers
num1 = float(sys.argv[1])
num2 = float(sys.argv[2])

# Compare and print result
if num1 > num2:
    print(num1, "is greater")
elif num2 > num1:
    print(num2, "is greater")
else:
    print("Both numbers are equal")
