# List Comprehension

# The General syntax for List comprehension
# --> Basic Transformation | new_list = [expression for item in iterable] | squares = [x**2 for x in range(5)] 

# --> Filtering with if | new_list = [expression for item in iterable if condition] | evens = [x fo x in range(10) if x%2==0] 

# --> Conditional Mapping with if-else | new_list = [expression_if_true if condition else expression_if_false for item in iterable] | even_odd = ["Even" if x%2==0 else "Odd" for x in range(4)]

# --> Multiple Filters | new_list = [expression for item in iterable if condition1 if condition2] | multiple = [x for x in range(20) if x%2==0 if x%3==0] --> You can chain multiple if conditions at the end. These act like an and operation—the item is only included if all conditions are true.

# Nested Loops(Flattening) | new_list = [expression for outer_item in outer_iterable for inner_item in inner_iterable] | example = [num for row in [[1,2], [3,4]] for num in row]

# Nested List Comprehension | new_list = [[expression for inner_item in inner_iterable] for outer_item in outer_iterable] | example = [[j for j in range(3)] for i in range(3)] 
 
scores = [33, 25, 76, 69, 58, 84, 88, 90, 90.88, 64, 25, 26]

high_risks = [i for i in scores if i > 75]

print(high_risks)