import socket
import sys

def run_server():
    host = '127.0.0.1'  # Localhost
    port = 5000         # Arbitrary non-privileged port

    # Create a TCP/IP socket
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Allow immediate reuse of the port after stopping the server
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"[SERVER] Listening on {host}:{port}...")
    except socket.error as e:
        print(f"[SERVER] Socket setup or binding failed: {e}")
        sys.exit(1)

    try:
        # Wait for an incoming connection
        connection, client_address = server_socket.accept()
        print(f"[SERVER] Connection established with {client_address}")

        try:
            # Receive data (up to 1024 bytes)
            data = connection.recv(1024)
            if data:
                # Decode the bytes back into a readable string
                message = data.decode('utf-8')
                print(f"[SERVER] Received message: {message}")
            else:
                print("[SERVER] Client disconnected without sending data.")
        except socket.error as e:
            print(f"[SERVER] Error receiving data: {e}")
        finally:
            # Clean up the client connection
            connection.close()
            print("[SERVER] Client connection closed.")

    except KeyboardInterrupt:
        print("\n[SERVER] Shutting down server manually.")
    finally:
        # Clean up the main server listening socket
        server_socket.close()
        print("[SERVER] Server socket closed.")

if __name__ == '__main__':
    run_server()
import socket
import sys


def run_client():
    host = '127.0.0.1'
    port = 5000
    message = "Hello from client!"

    # Create a TCP/IP socket
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print(f"[CLIENT] Failed to create socket: {e}")
        sys.exit(1)

    # Connect to the server and send the message
    try:
        print(f"[CLIENT] Connecting to {host}:{port}...")
        client_socket.connect((host, port))
        print("[CLIENT] Connected successfully.")

        # Send the string converted into bytes
        client_socket.sendall(message.encode('utf-8'))
        print(f"[CLIENT] Sent message: '{message}'")

    except socket.gaierror as e:
        print(f"[CLIENT] Address-related error connecting to server: {e}")
    except socket.error as e:
        print(f"[CLIENT] Network connection error: {e}")
    finally:
        # Always guarantee socket closure to free system resources
        client_socket.close()
        print("[CLIENT] Socket closed.")


if __name__ == '__main__':
    run_client()
