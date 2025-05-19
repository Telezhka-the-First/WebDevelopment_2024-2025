import socket

def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    client_socket.sendall("Hello, server".encode('utf-8'))
    print(client_socket.recv(1024).decode('utf-8'))

    client_socket.close()

if __name__ == "__main__":
    run_client()
