import socket
SERVER_IP ="192.168.1.15"
SERVER_PORT =8080
size =1024
if __name__ == "__main__":
    sock =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    address =(SERVER_IP,SERVER_PORT)
    sock.connect(address)
    rev =sock.recv(size)
    print(rev.decode())
    sock.close()

