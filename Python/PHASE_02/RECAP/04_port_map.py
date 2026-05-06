# Dictionaries: Mappping Services and Ports

port_dictionary = {
    80 : 'http',
    443: 'https',
    22 : 'ssh'
}

while True:
    try:
        user_port = int(input("Enter a port number: "))
        break
    except ValueError:
        print("Please enter a valid port number!")

service_name = port_dictionary.get(user_port)

if service_name:
    print(f"Port {user_port} uses {service_name.upper()}")
else:
    print(f"No service found for port {user_port}")