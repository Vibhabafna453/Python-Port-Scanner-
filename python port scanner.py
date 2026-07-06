import socket
target = input("Enter IP Address: ")

ports = [22, 23, 25, 53, 55, 80, 110, 443]

print("\nScanning", target)
print("-" * 30)

for port in ports:
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)

    result = scanner.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} : OPEN")
    else:
        print(f"Port {port} : CLOSED")

    scanner.close()

print("-" * 30)
print("Scanning completed!")

#only scan hostename and IP