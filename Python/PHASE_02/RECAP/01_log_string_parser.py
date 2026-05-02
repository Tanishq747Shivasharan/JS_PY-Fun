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
