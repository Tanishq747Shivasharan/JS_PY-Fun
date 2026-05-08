# Strings: Working with Textual Data

# sample_stringMsg = '2026-04-13 ERROR: Unauthorized access attempt at 192.168.1.1'

# use this to see which all methods of string are present in python.
# print(dir(sample_stringMsg))
# also you can use this to get a thorough understanding of string methods/functions
# print(help(str))

# error = sample_stringMsg[11: 16]
# print(error)

# ip = sample_stringMsg[49:]
# print(ip)

# practice from Day 2 : 30 Days of python programming --> https://github.com/asabeneh/30-days-of-python

firstName = 'Naruto'
lastName = ' Uzumaki'
fullName = firstName + lastName
country = 'Japan'
city = 'Tokyo'
age = 21
year = '2007'
is_married = True
is_true = True
is_light_on = False

FirstName, LastName, Age, country = 'Minato', 'Namikaze', '52', '1996'
print(FirstName,lastName, age, country)

print(type(firstName))
print(type(LastName))
print(type(fullName))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(firstName))
print(len(firstName) > len(lastName))

num_one, num_two = 23, 10
total = num_one + num_two
print(f'{num_one} + {num_two} = {total}' )

diff = num_two - num_one
print(f'{num_two} - {num_one} = {diff}' )

product = num_two * num_one
print(f'{num_two} x {num_one} = {product}' )

division = num_one / num_two
print(f'{num_one} / {num_two} = {division}' )

reminder = num_two % num_one
print(f"{num_two} % {num_one} = {reminder}")

exp = num_one ** num_two
print(f'{num_one}^{num_two} = {exp}')

floor_division = num_one // num_two
print(f"{num_one} floor division {num_two} = {floor_division}")

r = 30
area_of_circle = 3.14 * r ** 2
circum_of_circle = 2 * 3.14 * r
print(f"Area of circle(Static value): {area_of_circle}")
print(f"Circumference of circle(Static value): {circum_of_circle}")
user_r = int(input("Enter custom radius to calculate the area of circle: "))
area_of_ucircle = 3.14 * user_r ** 2
print(f"The area of user defined radius circle is: {area_of_ucircle}")

firstn = input("Enter first name: ")
lastn = input("Enter last name: ")
cnt = input("Enter country name: ")
age = int(input("Enter your age: "))

print(f"{firstn, lastn, cnt, age}")

# Practice from Day 4 Strings in Python

t3 = 'Thirty'
d = 'Days'
o = 'Of'
p = 'Python'
print(t3, d, o, p)

company = "Coding For All"

print(company)

print(len(company))

upper_case = company.upper()
print(upper_case)

lower_case = company.lower()
print(lower_case)

first_letter_capital = company.capitalize()
title = company.title()
swapcase = company.swapcase()
print(f"{first_letter_capital}\n{title}\n{swapcase}")

print(company[7:22])

print(company.index('Coding'))

print(company.replace('Coding', 'Python'))