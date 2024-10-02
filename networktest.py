"""
Disclaimer

This code is intended for educational purposes only.
It is designed to help users understand Wi-Fi security and password management.
The creator of this code does not endorse or support any illegal activities, including unauthorized access to computer networks.
"""

import os
import time
import speedtest

def ping_test(host):
    print(f"Pinging {host}...")
    response = os.system(f"ping -c 4 {host}")  # Use -n on Windows

    if response == 0:
        print(f"{host} is reachable.")
    else:
        print(f"{host} is not reachable.")

def speed_test():
    print("Testing download and upload speed...")
    st = speedtest.Speedtest()

    print("Finding best server...")
    st.get_best_server()

    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000      # Convert to Mbps

    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")

if __name__ == "__main__":
    # Get user input for host
    host = input("Enter the host or IP address to ping (e.g., google.com): ")

    # Perform ping test
    start_time = time.time()
    ping_test(host)
    ping_duration = time.time() - start_time
    print(f"Ping test completed in {ping_duration:.2f} seconds.")

    # Perform speed test
    start_time = time.time()
    speed_test()
    speed_duration = time.time() - start_time
    print(f"Speed test completed in {speed_duration:.2f} seconds.")
