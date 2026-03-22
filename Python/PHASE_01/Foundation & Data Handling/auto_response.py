# Ternary Operator

unauthorized_attemts = int(input("Enter a random value between 1-10: "))

status = "Alert" if unauthorized_attemts > 5 else "Clear"

print(status)