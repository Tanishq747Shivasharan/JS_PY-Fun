# Loops and Iterations: Automated Port Sweeping

ports = [80, 24, 120, 442, 200, 22, 69, 202, 404]

for i in ports:
    if i == 22:
        print("Critical Service Found")
        break
