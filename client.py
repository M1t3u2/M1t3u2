import socket

def connect_to_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 8888))
    print("[*] Connecté au serveur VPN")

    # Logique du client VPN ici

if __name__ == "__main__":
    connect_to_server()
