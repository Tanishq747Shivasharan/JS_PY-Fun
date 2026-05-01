# Strings: Working with Textual Data

sample_stringMsg = '2026-04-13 ERROR: Unauthorized access attempt at 192.168.1.1'

# use this to see which all methods of string are present in python.
# print(dir(sample_stringMsg))
# also you can use this to get a thorough understanding of string methods/functions
# print(help(str))

error = sample_stringMsg[11: 16]
print(error)

ip = sample_stringMsg[49:]
print(ip)