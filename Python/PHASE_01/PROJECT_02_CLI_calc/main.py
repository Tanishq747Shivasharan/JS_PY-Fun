def calculate(num1, num2, operator):
    operations = {
        "+": (num1 + num2, "+"),
        "-": (num1 - num2, "-"),
        "*": (num1 * num2, "×"),
        "/": (num1 / num2 if num2 != 0 else None, "/")
    }
    
    if operator not in operations:
        return None, "invalid"
    
    result, symbol = operations[operator]
    if result is None:
        return None, "zero_division"
    
    n1 = int(num1) if num1 == int(num1) else num1
    n2 = int(num2) if num2 == int(num2) else num2
    res = int(result) if result == int(result) else result
    
    return f"{n1} {symbol} {n2} = {res}", "success"


while True:
    print("\n" + "=" * 35)
    print("       SIMPLE CALCULATOR")
    print("=" * 35)
    
    try:
        user_input = input('First number (or "q" to quit): ').strip().lower()
        if user_input == "q":
            print("Bye!")
            break
        
        num1 = float(user_input)
        num2 = float(input("Second number: ").strip())
        operator = input("Operation (+ - × /) or q: ").strip()
        
        if operator.lower() == "q":
            print("Bye!")
            break
            
    except ValueError:
        print(" Error: Please enter valid numbers!")
        continue
    
    result, status = calculate(num1, num2, operator)
    
    if status == "invalid":
        print(" Invalid operator! Use: + - * /")
    elif status == "zero_division":
        print(" Cannot divide by zero!")
    else:
        print(f"\n Result: {result}")