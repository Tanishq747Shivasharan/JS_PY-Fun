# String Methods & Slicing

log_entry = "ERR_404_NOT_FOUND"

print(f"The error code is: {log_entry[4:7]}")

# Best way of extraction is using the .split() method with an underscore '-' as the separator to turn the string into a list of segments.
# And then accessing the segments: if you use the split method, retrive the error code by accessing the second item in the resulting list, which is at index 1.abs
print(f"The error code is: {log_entry.split('_')[1]}")
# Like this 👆