from socket import *

addr = tuple(input("Insira o endereço: "))

for port in range(0,1000):
    s = socket(AF_INET(addr, port), SOCK_STREAM)
    if (s.connect_ex(addr)) == 0:
        print(f"Porta {port} Aberta")
    else:
        print(f"Porta {port} Fechada")
    s.close()