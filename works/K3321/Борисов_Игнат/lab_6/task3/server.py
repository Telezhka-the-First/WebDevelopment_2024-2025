import socket

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(1)

    while True:
        conn, addr = server_socket.accept()
        request = conn.recv(1024)

        with open("index.html", "r", encoding="utf-8") as f:
            content = f.read()

        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html; charset=utf-8\r\n"
            f"Content-Length: {len(content.encode('utf-8'))}\r\n"
            "\r\n"
            + content
        )
        conn.sendall(response.encode('utf-8'))
        conn.close()

if __name__ == "__main__":
    run_server()
