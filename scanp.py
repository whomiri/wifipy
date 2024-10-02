import os
import platform
import subprocess
from concurrent.futures import ThreadPoolExecutor

# Determine the target IP address range
network_prefix = input("Enter network address prefix (e.g. 192.168.1): ")

# Ping func
def ping_device(ip):
    # Operating system is determined
    param = "-n" if platform.system().lower() == "windows" else "-c"
    
    # Ping command
    command = ["ping", param, "1", ip]
    
    response = subprocess.call(command, stdout=subprocess.PIPE)
    if response == 0:
        print(f"{ip} active")
    else:
        print(f"{ip} inaccessible")

# Determining IP range to ping all devices on the network
ip_range = [f"{network_prefix}.{i}" for i in range(1, 255)]

# Use threads to ping multiple devices at the same time
with ThreadPoolExecutor(max_workers=50) as executor:
    executor.map(ping_device, ip_range)

print("\nCompleted the scan.")
