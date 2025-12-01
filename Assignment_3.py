#Task_1
number = int(input("Enter the number: "))
def factorial(num):
    if num == 1:
        return 1
    else:
        fact = num * factorial(num - 1)
        return fact
print(f"Factorial of {number} is: {factorial(number)}")

#Task_2
import math
number1 = int(input("Enter a number: "))
output1 = math.sqrt(number1)
output2 = math.log(number1)
output3 = math.sin(number1)
print(f"Square root: {output1}")
print(f"Logarithm: {output2}")
print(f"Sine: {output3}")
