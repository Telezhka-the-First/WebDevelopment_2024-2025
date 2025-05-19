import socket

def parallelogram_area(base, height):
    return base * height

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 1234))
    server_socket.listen(1)

    conn, addr = server_socket.accept()

    data = conn.recv(1024).decode('utf-8')
    base, height = map(float, data.split())
    area = parallelogram_area(base, height)
    conn.sendall(str(area).encode('utf-8'))

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    run_server()
