#Day 2: 30 Days of python programming

first_name = 'Collins'
last_name = 'Wamucii'
full_name = 'Collins Wamucii'
country = 'Kenya'
city = 'Nairobi'
age = 22
year = 2024
is_married = False
is_true = True
is_light_on = False
todays_day, todays_month, todays_year = 24, 'September', 2024
print('My name is:', full_name, 'and I live in', city,',', country)
print('Today is ', todays_day, todays_month, todays_year)

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(todays_day))
print(type(todays_month))
print(type(todays_year))

# Compare the length of first_name and last_name
if len(first_name) > len(last_name):
    print("First name is longer than last name.")
elif len(first_name) < len(last_name):
    print("Last name is longer than first name.")
else:
    print("First name and last name are of the same length.")

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two
print(total, diff, product, division, remainder, exp, floor_division)

radius = 30
area_of_circle = 3.142 * radius ** 2
circum_of_circle = 2 * 3.142 * radius
print(area_of_circle, circum_of_circle)

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
country = input('Enter your country: ')
age = input('Enter your age: ')

print(first_name, last_name, country, age)

help('keywords')

# Day 2: 30 Days of python programming