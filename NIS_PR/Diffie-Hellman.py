#These two are public knowledge.
# p > g
p = int(input("Enter the prime number p:"))
g = int(input("Enter a generating number g key: "))

user_a = int(input("Enter a secret integer for a: "))
user_b = int(input("Enter a secret integer for b: "))

#This is what will be passed over a public channel
# A = (g**user_a) % p | alternative syntax for getting the same result.
A = pow(g, user_a, p)
B = (g**user_b) % p

print("A:", A, "B:", B)

sec_a = (B**user_a) % p
print("Shared key is:", sec_a)

# sec_b = (A**user_b) % p | alternative syntax for getting the same result.
sec_b = pow(A, user_b, p)
print("Shared key is:", sec_b)
