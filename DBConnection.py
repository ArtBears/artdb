import socket
import sqlvalidator


def is_valid(data: bytes):
    decoded_data = data.decode('utf-8')
    validated_data = sqlvalidator.parse(decoded_data)
    return validated_data.is_valid()

class DBConnection:
    HOST = '0.0.0.0'
    PORT = 51783
    

    # TODO add arguments for host and port so that they can pass in their own values
    def __init__(self) -> None:
        self.connect()

    def connect(self):
        #TODO check if port is already in use

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            try:
                address : socket._Address= (self.HOST, self.PORT)
                server_socket.bind(address)
                server_socket.listen(4)
                
                print(f'Server is listening on {self.HOST}:{self.PORT}')
                
                while True:
                    client_socket, client_address = server_socket.accept()
                    print(f'Accepted connection from {client_address}')

                    data = client_socket.recv(4096)
                    if data == b'stop':
                        response = "Shutting down server"
                        client_socket.send(response.encode('utf-8'))
                        client_socket.close()
                        server_socket.close()
                        break
                    
                    # TODO validate the query data
                    if is_valid(data):
                        response = "Is valid sql"
                        client_socket.send(response.encode('utf-8'))
                        # TODO run the sql query
                    elif is_valid(data) == False:
                        response = "Is NOT valid sql"
                        client_socket.send(response.encode('utf-8'))
                    else:
                        response = f"Recieved: {data.decode('utf-8')}"
                        client_socket.send(response.encode('utf-8'))

                    client_socket.close()
                server_socket.close()
            except ConnectionAbortedError:
                client_socket.close()
                server_socket.close()



class Client:
    HOST = 'localhost'
    PORT = 51783

    
    def __init__(self, host=HOST, port=PORT) -> None:
        if host:
            self.HOST = host
        if port:
            self.PORT = port  

    def connect(self):
        # figure out how to close socket after each response and create a new one
        while True:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                try:
                
                    client_socket.connect((self.HOST, self.PORT))
                    message = input('Enter a message (or exit to quit): ')
                    if message == 'exit':
                        break

                    client_socket.send(message.encode('utf-8'))

                    response = client_socket.recv(4096)
                    print(f'Server response {response.decode("utf-8")}')
                    client_socket.close()
                except ConnectionAbortedError as e:
                    print(f'Connection aborted: {e}')
                except ConnectionRefusedError as e:
                    print('Server Socket is closed')
                    break
                finally:
                    client_socket.close()
            