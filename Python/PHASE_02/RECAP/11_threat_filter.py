# List Comprehensions: Rapid Threat Filtering

scores = [21, 33, 34, 69, 80, 89, 99, 58]

Risk_lists = [item for item in scores if item > 80]

print(Risk_lists)