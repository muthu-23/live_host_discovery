# 🛰 Live Host Discovery

A Python-based tool designed to detect live hosts in a given IP range using ICMP ping (echo requests). Ideal for cybersecurity learners and network administrators, this utility scans a local subnet and identifies which devices are active and reachable.

---

## 📌 Project Overview

This tool sends ICMP echo requests to each IP address in a specified range (CIDR format) to identify which hosts are up. It is useful for mapping devices connected to a private network, such as home or lab setups, and assists in network diagnostics or penetration testing.

---

## ✨ Features

✅ Accepts user input for CIDR IP range (e.g., 192.168.1.0/24)  
✅ Scans the entire subnet and pings all IPs individually  
✅ Displays active (reachable) IPs in a clean output  
✅ Fast, CLI-based and beginner-friendly implementation  
✅ Error handling for unreachable hosts and exceptions 

---

## 🧰 Technologies Used

- *Python 3.x* – Programming Language  
- *ipaddress* – For generating the range of IP addresses  
- *subprocess* – To execute ping commands and capture responses

---

## ⚙ Requirements

- Python 3.x installed
- Basic networking knowledge (IP addressing, CIDR, ping)
- LAN/WiFi connection (for scanning within local subnet)

---

## 🚀 How It Works

1. User provides a valid CIDR IP range as input.
2. The script splits the range into individual IPs.
3. Each IP is pinged using ICMP echo requests.
4. If a reply is received, the host is marked as "UP".
5. Output is shown in the console.

---

## 💻 Sample Output

Enter the IP range (e.g., 192.168.1.0/24): 192.168.1.0/24

Scanning live hosts in 192.168.1.0/24 ... 

Host 192.168.1.12 is UP

Host 192.168.1.15 is UP Host 192.168.1.22 is UP

---

## 📁 File Structure

live_host_discovery/
  ├── live_host_discovery.py     
  └── README.md                  

---

## 👨‍💻 Author

*Muthusamy T*  
B.Sc Cybersecurity Student  
Vels University, Chennai (Pallavaram)  
GitHub: [muthu-23]

⚠ Legal & Ethical Notice

This tool is intended *only for educational or authorized network use. Do **not* scan public or unauthorized networks without proper consent. Unauthorized use may violate privacy laws or institutional policies.
