# Loops: While & For

interesting_port = [22, 445, 80, 53, 25, 110, 143]

for i in range(1, 1024):
    if i in interesting_port:
        print(f"Port {i} is interesting")
