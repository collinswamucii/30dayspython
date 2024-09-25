#Day 3 of 30 Days of Python Programming

age = 22
height = 1.88
complex_number = 1 + 1j

#Script to calculate the area of a triangle
base = float(input('Enter the base of the triangle: '))
height = float(input('Enter the height of the triangle: '))
area = 0.5 * base * height
print('The area of the triangle is', area)

#script to calculate the perimeter of a triangle
side_a = float(input('Enter the length of side a: '))
side_b = float(input('Enter the length of side b: '))
side_c = float(input('Enter the length of side c: '))
perimeter = side_a + side_b + side_c
print('The perimeter of the triangle is', perimeter)

#Question 6
length = float(input('Enter the length of the rectangle: '))
width = float(input('Enter the width of the rectangle: '))
area1 = length * width
perimeter1 = 2 * (length + width)
print('The area of the rectangle is', area1)
print('The perimeter of the rectangle is', perimeter1)

#Question 7
radius = float(input('Enter the radius of the circle: '))
area2 = 3.142 * radius ** 2
circumference = 2 * 3.142 * radius
print('The area of the circle is', area2)
print('The circumference of the circle is', circumference)

#Question 8
# Calculate the slope, x-intercept, and y-intercept of y = 2x - 2
slope = 2
y_intercept = -2
x_intercept = -y_intercept / slope

print('The slope is', slope)
print('The y-intercept is', y_intercept)
print('The x-intercept is', x_intercept)

#Question 9
x1, y1 = 2, 2
x2, y2 = 6, 10

slope = (y2 - y1) / (x2 - x1)
euclidean_distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print('The slope between the points is', slope)
print('The Euclidean distance between the points is', euclidean_distance)
