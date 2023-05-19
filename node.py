import socket
import threading

# threading.Thread(target=thread_function, args=(1,))
# x.start()

SERVER_IP = '192.168.1.2'
SERVER_PORT = 5305

MY_IP = '127.0.0.1'
MY_PORT = int(input("Enter node port: "))

"""
PROTOCOL:
GIMME METALICA.MP3
"""

class ClientThread(threading.Thread): 
    def __init__(self,ip,port, conn): 
        threading.Thread.__init__(self) 
        self.ip = ip
        self.port = port
        self.conn = conn
        print ("[+] New client socket thread started for " + ip + ":" + str(port))
    
    def run(self): 
        try:
            while True:
                data = self.conn.recv(1024)
                print("Client sent data:", data.decode())
                self.conn.sendall("kova".encode())
        except Exception as e:
            print("Client probably disconnected")

class ServerThread(threading.Thread):
    def __init__(self,ip,port, conn): 
        threading.Thread.__init__(self) 
        self.ip = ip
        self.port = port
        self.conn = conn
        print ("[+] New server socket thread started for " + ip + ":" + str(port))
    
    def run(self): 
        try:
            while True:
                data = self.conn.recv(1024)
                print("Server sent data:", data.decode())
                self.conn.sendall("kova".encode())
        except Exception as e:
            print("Server probably disconnected")

def main():
    listening_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_address = (MY_IP, MY_PORT)
    listening_sock.bind(my_address)
    listening_sock.listen(4)
    threads = []
    
    server_socket = socket.socket()  # instantiate
    server_socket.connect((SERVER_IP, SERVER_PORT))  # connect to the server
    newthread = ServerThread(SERVER_IP,SERVER_PORT,server_socket)
    newthread.start()

    while True:
        try:
            listening_sock.listen(1)
            (conn, (ip,port)) = listening_sock.accept()
            newthread = ClientThread(ip,port, conn)
            newthread.start()
            threads.append(newthread)
        except Exception as e:
            continue
    client_socket.close()  # close the connection
if __name__ == '__main__':
    main()