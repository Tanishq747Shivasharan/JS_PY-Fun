# Dictionaries

net_port = { 
    21: "FTP",
    22: "SSH/SFTP",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP",
    68: "DHCP",
    80: "HTTP",
    110: "POP3",
    123: "NTP",
    143: "IMAP",
    443: "HTTPS",
    993: "IMAPS",
    995: "POP3S"
 }

get_service = net_port.get(int(input("Enter a port number to find: ")), "Unknown")
print(get_service)