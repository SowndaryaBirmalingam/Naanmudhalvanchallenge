def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
# Example usage
num = 5
result = factorial(num)
print(f"The factorial of {num} is {result}")
 # Get input from user
year = int(input("Enter a year: "))
# Check if it's a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")