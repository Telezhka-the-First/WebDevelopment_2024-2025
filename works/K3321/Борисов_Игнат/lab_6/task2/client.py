import socket

def run_client():
    base = input("Введите длину основания: ")
    height = input("Введите высоту: ")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 1234))

    message = f"{base} {height}"
    client_socket.sendall(message.encode('utf-8'))

    result = client_socket.recv(1024).decode('utf-8')
    print("Площадь:", result)

    client_socket.close()

if __name__ == "__main__":
    run_client()
