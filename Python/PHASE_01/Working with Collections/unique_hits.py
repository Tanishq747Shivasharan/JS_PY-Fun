# Sets

ip_list1 = ["192.168.1.12", "192.168.1.30", "17.168.10.1", "168.12.1.69"]
ip_list2 = ["192.168.1.12", "191.168.1.30", "27.168.10.1", "168.12.1.63"]

set1 = set(ip_list1)
set2 = set(ip_list2)

print("IP's present in both the sets")
intersection = set1 & set2
print(intersection)