# Modules & Standard Lib

# In cybersecurity, we often calculate "entropy" (randomness). Instead of writing complex math yourself,so using Python’s built-in math module to find the square root of an entropy score.

from math import sqrt
# OR import math --> So that we can use any method in the math module(pre-built).

entropy_value = 64
print(f"The entropy value is: {sqrt(entropy_value)}")