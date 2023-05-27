import socket

HOST = '192.168.0.68'  # IP address of the server
PORT = 12345  # Port number to connect to

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

while True:
    # Get command input from the user
    command = input("Enter command ('hello', 'quit'): ")

    # Send the command to the server
    client_socket.send(command.encode())

    if command == "quit":
        break

# Close the client socket
client_socket.close()
