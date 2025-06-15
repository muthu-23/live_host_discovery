import ipaddress
import subprocess

def scan_live_hosts(network):
    try:
        ip_net = ipaddress.ip_network(network, strict=False)
    except ValueError:
        print("Invalid network. Please enter a valid CIDR format (e.g., 192.168.1.0/24).")
        exit()

    print(f"\nScanning live hosts in {network}...\n")
    for ip in ip_net.hosts():
        ip = str(ip)
        try:
            result = subprocess.run(["ping", "-n", "1", "-w", "500", ip], stdout=subprocess.DEVNULL)
            if result.returncode == 0:
                print(f"✅ Host {ip} is UP")
        except Exception as e:
            print(f"❌ Error scanning {ip}: {e}")

def main():
    network = input("Enter the IP range (e.g., 192.168.1.0/24): ")
    scan_live_hosts(network)

if __name__ == "__main__":
    main()