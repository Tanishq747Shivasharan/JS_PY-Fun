# Formatted String Literals also called as f-strings for short
# Let you include the value of Python expressions inside a string by prefixing the string with f or F and writing expressions as {expression}.

# An optional format specifier can follow the expression. This allows greater control over how the value is formatted. The following example rounds pi to three places after the decimal:
import math
print(f"The value of pi is approximately {math.pi:.3f}")

stud_dictionary = {
    'name': 'Tanishq',
    'age': 18,
    'skill': 'Python'
}
for key, value in stud_dictionary.items():
    print(f'{key:10} ==> {value:10}')

# Other modifiers include '!a' applies ascii(), '!s' applies str(), and '!r' applies repr():
thought = 'Python is crazy!'
print(f"The person who thinks has nothing to think about expect {thought!r}")
print(f"The person who thinks has nothing to think about expect {thought!a}")
print(f"These are just random number {69!s}")

# The = specifier can be used to expand an expression to the text of the expression, an equal sign, then the representation of the evaluated expression:

last_name = 'Shivasharan'
first_name = 'Tanishq'
middle_name = 'Shekhar'
print(f"My full name is: {last_name=} {first_name=} {middle_name=}")
