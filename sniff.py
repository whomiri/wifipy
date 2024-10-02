"""
DISCLAIMER
This code is intended for educational purposes only.
It is designed to help users understand Wi-Fi security and password management.
The creator of this code does not endorse or support any illegal activities, including unauthorized access to computer networks.
"""

from scapy.all import sniff

def packet_callback(packet):
    # Print packet summary
    print(packet.summary())

def start_monitoring(interface):
    print(f"Starting packet capture on interface: {interface}")
    # Capture packets and call packet_callback for each captured packet
    sniff(iface=interface, prn=packet_callback, store=0)

if __name__ == "__main__":
    # Specify the network interface to monitor
    interface = input("Enter the network interface to monitor (e.g., wlan0, eth0): ")
    start_monitoring(interface)
