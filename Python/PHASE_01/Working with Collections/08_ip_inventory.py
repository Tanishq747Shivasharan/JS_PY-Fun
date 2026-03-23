# List and Methods

ip_list = ["192.168.1.1", "10.1.1.1", "172.16.1.1"]
print("This is initial created list")
print(ip_list,"\n")

ip_list.append("10.1.1.2")
print("Added one ip as \"10.1.1.2\"")
print(ip_list,"\n")

ip_list.extend(["10.1.1.3", "10.1.1.4"]) # Appending another list
print("Appending another list to the existing list using .extend method!")
print(ip_list,"\n")

ip_list.pop()
print("removing the top most or the most recent ip from the list using .pop method!")
print(ip_list, "\n")

print("""
Python List Methods:

Core Methods:
- append(x): Add element to end
- extend(iterable): Add multiple elements to end  
- insert(i, x): Insert at index i
- remove(x): Remove first occurrence of x
- pop([i]): Remove/return element at index i

Search Methods:
- index(x): Find first occurrence index
- count(x): Count occurrences of x

Modify Methods:
- clear(): Remove all elements
- copy(): Shallow copy of list
- reverse(): Reverse list in place
- sort(): Sort list in place
""")