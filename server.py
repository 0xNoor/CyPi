import socket
import os

HOST = '0.0.0.0'  # IP address of the server
PORT = 12345  # Port number to listen on

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)

print("Server listening on {}:{}".format(HOST, PORT))

# Accept a client connection
client_socket, client_address = server_socket.accept()
print("Client connected:", client_address)

while True:
    # Receive command from the client
    command = client_socket.recv(1024).decode()

    # Process the command
    if command == "hello":
        print("Command received: hello")
        os.system("python sensordata.py")
        # Add your code here to perform the corresponding action for the command

    elif command == "quit":
        print("Command received: quit")
        break

# Close the client socket and server socket
client_socket.close()
server_socket.close()
