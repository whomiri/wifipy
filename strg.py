import os
import socket
import time

def ping_test(host):
    print(f"Pinging {host}...")
    response = os.system(f"ping -c 4 {host}")  # Use -n on Windows

    return response == 0

def port_scan(host, start_port, end_port):
    open_ports = []
    print(f"Scanning ports from {start_port} to {end_port} on {host}...")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    
    return open_ports

def generate_report(host, ping_result, open_ports):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    report_filename = f"security_test_report_{host.replace('.', '_')}.txt"

    with open(report_filename, 'w') as report_file:
        report_file.write(f"Security Test Report for {host}\n")
        report_file.write(f"Timestamp: {timestamp}\n\n")
        report_file.write(f"Ping Test Result: {'Reachable' if ping_result else 'Not Reachable'}\n")
        
        report_file.write("Open Ports:\n")
        if open_ports:
            for port in open_ports:
                report_file.write(f"- Port {port} is open.\n")
        else:
            report_file.write("No open ports found.\n")

    print(f"Report generated: {report_filename}")

if __name__ == "__main__":
    # Get user input for host and port range
    host = input("Enter the host or IP address to test (e.g., google.com): ")
    start_port = int(input("Enter the starting port for scanning (e.g., 20): "))
    end_port = int(input("Enter the ending port for scanning (e.g., 80): "))

    # Perform ping test
    ping_result = ping_test(host)

    # Perform port scan
    open_ports = port_scan(host, start_port, end_port)

    # Generate security test report
    generate_report(host, ping_result, open_ports)
