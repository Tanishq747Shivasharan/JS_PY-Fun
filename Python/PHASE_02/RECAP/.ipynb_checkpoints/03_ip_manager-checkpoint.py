# List, Tuples, and Sets: Managing IP Inventoriesa

ip_ls1 = ["192.168.4", "192.168.1.3", "192.168.30", "192.168.33.15", "10.12.0.24"]
ip_ls2 = ["192.168.33.15", "14.12.25.225", "192.168.255.255", "192.168.1.3"]

set1 = set(ip_ls1)
set2 = set(ip_ls2)

print("IP's that are comman to both the server logs.")
print(set1.intersection(set2))