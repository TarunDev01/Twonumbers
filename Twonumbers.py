import sys

# Default values
default_num1 = 10
default_num2 = 20

# If two numbers are provided through command line
if len(sys.argv) == 3:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    print("Using command-line values...")
else:
    # Using defaults
    num1 = default_num1
    num2 = default_num2
    print("Using default values...")

# Compare and print result
if num1 > num2:
    print(num1, "is greater")
elif num2 > num1:
    print(num2, "is greater")
else:
    print("Both numbers are equal")
