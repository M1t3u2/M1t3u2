import socket
import threading

def handle_client(client_socket):
    # Gestion des clients ici
    pass

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 8888))
    server.listen(5)

    print("[*] Serveur VPN en écoute sur le port 8888")

    while True:
        client_socket, addr = server.accept()
        print(f"[*] Connexion acceptée de {addr[0]}:{addr[1]}")

        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()


def connect_to_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 8888))
    print("[*] Connecté au serveur VPN")

    # Logique du client VPN ici

if __name__ == "__main__":
    connect_to_server()
