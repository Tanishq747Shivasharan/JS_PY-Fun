# Just an unprofessional worm simulation program.
# Just does Autonomous scanning, No exploitation, No self-replication It's just an recon.
import socket

def scan(ip, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((ip, port))
        return True
    except:
        return False

for i in range(1, 5):
    target_ip = f"192.168.1.{i}"
    if scan(target_ip, 80):
        print(f"Open service on {target_ip}")
