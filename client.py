import socket
SERVER_IP ="YOUR IP"
SERVER_PORT =8080
if __name__ == "__main__":
    sock =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    address =(SERVER_IP,SERVER_PORT)
    sock.connect(address)
    rev =sock.recv(1024)
    print(rev.decode())
    sock.close()

