# Functions: Reusable Security Tools

def validate_ip(ip):
    parts = ip.split(".")
    if len(parts) == 4:
        return True
    else:
        return False

ip = input("Enter any IPv4 address: ")
print(validate_ip(ip))