import socket

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)

    conn, addr = server_socket.accept()

    data = conn.recv(1024).decode('utf-8')
    if data == "Hello, server":
        print(data)
        conn.sendall("Hello, client".encode('utf-8'))

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    run_server()
