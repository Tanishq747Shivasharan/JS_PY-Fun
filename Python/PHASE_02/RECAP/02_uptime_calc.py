# Integers and Floats: Numeric Security Data

# total_seconds = 345600
# uptime_hours = total_seconds/3600

# final_report = round(uptime_hours)

# print(f"Server uptime: {final_report} hours")

age = 18
height = 6.0
compx = 5+6j

base = int(input("Enter base: "))
height = int(input("Enter height: "))
area = 0.5 * base * height
print(f"The are of the triangle is {area}")

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
perimeter = a + b + c
print(f"The perimeter of the triangle is {perimeter}")

length = float(input("Enter length of a rectangle: "))
width = float(input("Enter width of a rectangle: "))
area_of_rect = length * width
perimeter_of_rect = 2 * (length + width)
print(f"The area of rectangle is {area_of_rect}")
print(f"The perimeter of rectangle is {perimeter_of_rect}")

pi = 3.14
radius = float("Enter radius of a circle: ")
area_of_circle = pi * r * radius
circum_of_circle = 2 * pi * radius
print(f"The area of circle is {area_of_circle}\n The circumference of circle is {circum_of_circle}")

m =2 # Slope
c = -2
print(f"Slope ={m}")
y_intercept = c
print(f"y-intercept ={y_intercept}")
x_intercept = -c/m
print(f"x-intercept ={x_intercept}")

x1 = 2
y1 = 2
x2 = 6
y2 = 10
slope = (y2-y1)/(x2-x1)
print(f"Slope = {slope}")
d = ((x2-x1)**2 + (y2-y1)**2) ** 0.5
print(f"Distance = {d}")

if m == slope:
    print("Both the slopes are equal")
elif m > slope:
    print("The first calculated slope is greater then the second!")
else:
    print("The second calculated slope is greater then the first!")

x = -3
y = x*x + 6*x + 9
print(f"y={y}")
if y==0:
    print("y becomes 0 at x={x}")

sen = "I hope this course is not full of jargon."
if "jargon" in sen:
    print("Jargon exists in the sentence.")

val = "python"
len_val = len(val)
print(len_val)
float_len = float(len_val)
print(type(val))
final_string = str(len_val)
print(repr(final_string))

num = int(input("Enter a number: "))
if(num%2==0):
    print("The entered number is even")
else:
    print("The entered number is odd.")

div = 7 // 3
if(div == int(2.7)):
    print("Value is equal!")

str_num = "10"
num = 10
if(type(str_num) == type(num)):
    print("Both have equal types!")
else:
    print(f"Not equal {type(str_num)} | {type(num)}")

if(int(9.8) == 10):
    print(True)
else:
    print(False)