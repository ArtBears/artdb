import argparse
import socket

parser = argparse.ArgumentParser(description='A DBMS written in python')

parser.add_argument('--s', '--start', default=True, help='Start the dbms')
args = parser.parse_args()
print(args)
class DBConnection:
    HOST = '0.0.0.0'
    PORT = 51783
    
    def __init__(self) -> None:
        self.connect()

    def connect(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        address : socket._Address= ((self.HOST, self.PORT))
        server_socket.bind(address)
        server_socket.listen(1)
        
        print(f'Server is listening on {self.HOST}:{self.PORT}')
        
        while True:
            client_socket, client_address = server_socket.accept()
            print(f'Accepted connection from {client_address}')

            data = client_socket.recv(4096)
            if not data:
                break
            
            response = f"Recieved: {data.decode('utf-8  ')}"
            client_socket.send(response.encode('utf-8'))

            client_socket.close()
        server_socket.close()

def start_dbms():
    connection = DBConnection()

def main():
    
    start_dbms()

if __name__ == '__main__':
    main()