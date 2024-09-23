# Day one of 30 days of Python programming

print(3+2)  # Addition(+)
print(3-2)  # Subtraction(-)
print(3*2)  # Multiplication(*)
print(3/2)  # Division(/)
print(3**2)  # Exponentiation(**)
print(3%2)  # Modulus(%)
print(3//2)  # Floor division operator(//)

# Checking Data types
print(type(10))  # Int
print(type(3.14))  # Float
print(type(1 + 3j))  # Complex number
print(type('Collins'))  # String
print(type([1, 2, 3, 4]))  # List
print(type({'name': 'Collins', 'age': 23}))  # Dictionary
print(type({1, 2, 3, 4}))  # Set
print(type((1, 2, 3, 4)))  # Tuple

# Find an Euclidian distance between (2, 3) and (10, 8)
x1, y1 = 2, 3
x2, y2 = 10, 8
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(distance)