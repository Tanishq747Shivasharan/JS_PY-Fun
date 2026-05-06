# Dictionaries: Mappping Services and Ports

portDictionary = {
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

print(portDictionary.get(user_port, "service not found!"))