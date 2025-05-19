import socket
import threading

clients = []
nicknames = []

def broadcast(message, sender_conn):
    for client in clients:
        if client != sender_conn:
            try:
                client.send(message)
            except:
                client.close()
                remove_client(client)

def remove_client(client):
    if client in clients:
        index = clients.index(client)
        clients.remove(client)
        nickname = nicknames.pop(index)
        broadcast(f"{nickname} вышел из чата.".encode('utf-8'), None)
        print(f"Пользователь {nickname} отключился.")

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                remove_client(client)
                break
            broadcast(message, client)
        except:
            remove_client(client)
            break

def receive_connections():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen()

    print("Сервер запущен. Ожидание подключений...")

    while True:
        client, address = server_socket.accept()
        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Пользователь {nickname} подключился с {address}")
        broadcast(f"{nickname} вошел в чат.".encode('utf-8'), client)
        client.send("Подключение установлено. Добро пожаловать в чат!".encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    receive_connections()
