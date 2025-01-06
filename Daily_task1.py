1] Calculate the multiplication and sum of two numbers
# Function to calculate multiplication and sum
def calculate_operations(num1, num2):
    # Multiplication
    multiplication = num1 * num2
    
    # Sum
    total_sum = num1 + num2
    
    return multiplication, total_sum

# Example usage
num1 = 5
num2 = 3

multiplication_result, sum_result = calculate_operations(num1, num2)
print(f"Multiplication: {multiplication_result}")
print(f"Sum: {sum_result}")

-------------------------------------------------------------------------------------------------------------------
2] declare two variables and print that which variable is largest using ternary operators in python
# Declare two variables
num1 = 10
num2 = 20

# Use ternary operator to find the largest number
largest = num1 if num1 > num2 else num2

# Print the largest number
print(f"The largest number is: {largest}")

----------------------------------------------------------------------------------------------------------------------
3] python program to convert the temperature in degree centigrade to fahrenheit 
# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Example usage
celsius = 25  # You can change this value to any other temperature in Celsius
fahrenheit = celsius_to_fahrenheit(celsius)

# Print the result
print(f"{celsius}°C is equal to {fahrenheit}°F")

---------------------------------------------------------------------------------------------------------------------
4] python program to find the area of the triangle whose sides are given
import math
# Function to calculate area using Heron's formula
def area_of_triangle(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    
    # Calculate the area
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return area

# Example usage
a = 5
b = 6
c = 7

area = area_of_triangle(a, b, c)

# Print the result
print(f"The area of the triangle with sides {a}, {b}, and {c} is: {area:.2f}")


