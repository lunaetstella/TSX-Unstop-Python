'''Write a script that takes two numbers as input and prints whether
the first number is greater than, less than, or equal to the second
number.'''
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

if x == y:
    print("Both numbers are equal.")
elif x > y:
    print(f"{x} is greater than {y}.")
else:
    print(f"{x} is less than {y}.")
