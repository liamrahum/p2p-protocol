import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5232

def main():
    client_socket = socket.socket()  # instantiate
    client_socket.connect((SERVER_IP, SERVER_PORT))  # connect to the server
    while True:
        client_socket.send("Tapuz".encode())
        print(client_socket.recv(1024).decode())
        
if __name__ == "__main__":
    main()
