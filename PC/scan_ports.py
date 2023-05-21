import socket
import threading

def scan_ports(ip):
    open_ports = []

    # Define a helper function for port scanning
    def scan_port(port):
        try:
            # Create a socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set a timeout value of 1 second
            s.settimeout(1)
            # Attempt to connect to the IP address and port
            result = s.connect_ex((ip, port))
            # If the connection was successful, the port is open
            if result == 0:
                open_ports.append(port)
            # Close the socket
            s.close()
        except socket.error:
            pass

    # Create a thread for each port in the range
    threads = []
    for port in range(1, 65536):
        t = threading.Thread(target=scan_port, args=(port,))
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    return open_ports

# Example usage
target_ip = "10.10.11.213"

open_ports = scan_ports(target_ip)
print("Open ports:")
for port in open_ports:
    print(port)
