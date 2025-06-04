#!/usr/bin/env python3
"""
Client-Server Application with Serialization
"""

import socket
import json


def start_server(host='127.0.0.1', port=65432):
    """Start a server that receives serialized JSON data."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()

        print("Server is listening for connections...")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            data = b""
            while True:
                packet = conn.recv(4096)
                if not packet:
                    break
                data += packet

            try:
                received_dict = json.loads(data.decode('utf-8'))
                print("Received Dictionary from Client:")
                print(received_dict)
            except json.JSONDecodeError:
                print("Failed to decode JSON data")


def send_data(data_dict, host='127.0.0.1', port=65432):
    """Send a dictionary to the server after serializing it to JSON."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            json_data = json.dumps(data_dict)
            client_socket.sendall(json_data.encode('utf-8'))
    except ConnectionRefusedError:
        print("Connection to the server failed.")
