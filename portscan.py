import sys
import socket

ipAddr = sys.argv[1]

for ports in range (0, 1000):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if s.connect_ex((ipAddr, ports)) == 0:
        print(f"Port {ports} is Open!")
        s.close()
    else:
        print(f"Port {ports} is Closed!")
        s.close()