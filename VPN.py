#!/usr/bin/python3
import os, time
import getpass
import sherlock
import socket
import threading
import webbrowser
from fake_useragent import UserAgent




def handle_client(client_socket):
    
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

    

if __name__ == "__main__":
    connect_to_server()

def connect_to_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 8888))
    print("[*] Connecté au serveur VPN")

    

if __name__ == "__main__":
    connect_to_server()
    

def change_ip_address():
    while True:
        time.sleep(10)
        print("[*] Changement d'adresse IP...")
        

def handle_client(client_socket):
    
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
    change_ip_thread = threading.Thread(target=change_ip_address)
    change_ip_thread.start()

    start_server()
    
import socket
import threading
import time
import webbrowser
from fake_useragent import UserAgent

def change_ip_address():
    while True:
        time.sleep(10)
        print("[*] Changement d'adresse IP...")
        

def handle_client(client_socket):
    
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
    change_ip_thread = threading.Thread(target=change_ip_address)
    change_ip_thread.start()

    start_server()


