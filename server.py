import socket
SERVER_IP ="192.168.1.15"
SERVER_PORT =8080
address =(SERVER_IP,SERVER_PORT)
if __name__ =="__main__":
    sock =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(address)
    sock.listen(5)
    print("[+]waiting ......")
    cli_sock,cli_addrsock = sock.accept()
    msg ="HI I AM VIGNESH"
    cli_sock.send(msg.encode())
    cli_sock.close()
    sock.close()