import socket

def test_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = socket.connect_ex((ip, port))
    socket.close()

    if result == 0:
        print(f"Port {port} is Open!")
    else:
        print(f"Port {port} is Closed!")