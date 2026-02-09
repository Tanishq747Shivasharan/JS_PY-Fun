import os
import sys
import time
from collections import defaultdict
from scapy.all import sniff, IP

THRESHOLD = 35
print(f"THRESHOLD: "{THRESHOLD})

def packet_callback(packet):
    src_ip = packet[IP].src
    packet_count[src_ip] += 1
    current_time = time.time()
    time_intervel = current_time - start_time[0
    if time_intervel >= 1:
        for ip, count in list(packet_count.items()):
            if count > THRESHOLD:
                print(f"Blocking DoS attack from {ip}")
                os.system(f"iptables -A INPUT -s {ip} -j DROP")
                del packet_count[ip]
        start_time[0] = current_time

if __name__ == "__main__":
    packet_count = defaultdict(int)
    start_time = [time.time()]
    print("Starting DoS attack blocker...")
    sniff(prn=packet_callback, store=0)
