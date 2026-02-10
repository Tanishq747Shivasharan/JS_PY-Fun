# DoS Attack Detection and Blocking using Python & Scapy

## Overview
This project demonstrates a **basic Denial of Service (DoS) attack detection and prevention mechanism** using Python.  
The program monitors incoming network packets in real time and **blocks IP addresses** that send an unusually high number of packets within a short time interval.

This project is intended for **educational and laboratory purposes only**.

---

## Objective
- To monitor live network traffic
- To detect abnormal packet rates from a single IP
- To block suspicious IP addresses using firewall rules
- To understand packet sniffing and rate-based attack detection

---

## Concept Used
- Packet Sniffing
- Rate Limiting
- Firewall Rule Management
- DoS Attack Detection

---

## Technologies Used
- **Python 3**
- **Scapy** (Packet sniffing library)
- **iptables** (Linux firewall)
- **Linux OS (Ubuntu preferred)**

---

## System Requirements
- Linux Operating System
- Python 3.8 or above
- Root (sudo) privileges
- Active network interface

> This project will **not work on Windows** without a full Linux environment.

---

## Required Libraries
Install the required packages using:

```bash
sudo apt update
sudo apt install python3-scapy iptables -y
```

## Simulation guide
Switch to sudo mode and verify the requirements to run the script:
```bash
sudo su
┌──(tanishq㉿kali)-[~]
└─$ uname
Linux
┌──(tanishq㉿kali)-[~]
└─$ python3 --version
Python 3.13.9
┌──(root㉿kali)-[/home/tanishq]
└─# sudo apt update 
┌──(root㉿kali)-[/home/tanishq]
└─# iptables --version 
iptables v1.8.11 (nf_tables)
┌──(root㉿kali)-[/home/tanishq]
└─# mkdir dos_blocker
┌──(root㉿kali)-[/home/tanishq]
└─# cd dos_blocker 
┌──(root㉿kali)-[/home/tanishq/dos_blocker]
└─# nano DoS_blocker.py
```
> Paste the code from `DoS_blocker.py` in this file.

Save and exit (`Ctrl+O`, `Enter`, `Ctrl+X`).

Make the script executable:
```bash
┌──(root㉿kali)-[/home/tanishq/DoS_blocker]
└─# python3 dos_blocker.py
THRESHOLD: 35
Starting DoS attack blocker...
```
 > Now from another terminal or system flood your ip using this command for just simulating and just seeing the blocked ip for verification purpose.
 ```bash
┌──(root㉿kali)-[/home/tanishq/dos_blocker]
└─# sudo hping3 -S <your-ip> -p 80 --flood
Blocking DoS attack from 192.168.1.x
```
> To verify the blocking, check the iptables rules:
```bash
sudo iptables -L -n --> Verify blocked IPs
CTRL + C --> to stop the script
sudo iptables -F --> to flush the rules
```
