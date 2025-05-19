import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message == "NICK":
                client_socket.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("Ошибка соединения")
            client_socket.close()
            break

def write_messages(client_socket):
    while True:
        message = input()
        if message:
            client_socket.send(f"{nickname}: {message}".encode('utf-8'))

if __name__ == "__main__":
    nickname = input("Введите ваше имя: ")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    write_thread = threading.Thread(target=write_messages, args=(client_socket,))
    write_thread.start()
