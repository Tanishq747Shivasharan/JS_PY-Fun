# Dictionaries: Mappping Services and Ports

ip_Man = {
    80 : 'http',
    443: 'https',
    22 : 'ssh'
}

user_port = int(input("Enter a port number: "))

print(ip_Man.get(user_port, "service not found!"))