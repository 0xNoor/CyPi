import socket
import os
import speech_recognition as sr
import time
import sounddevice
import pyautogui

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
    if command == "speech":
        print("Command received: speech")
        r = sr.Recognizer()

    # Specify the audio source (e.g., microphone or audio file)
    # For microphone input, use sr.Microphone() as the source
    # For audio file input, use sr.AudioFile('audio_file.wav') as the source
        source = sr.Microphone(device_index=1)

    # Adjust for ambient noise (optional)
    # Uncomment the following line if you need to adjust for ambient noise
    # with source as source:


        print("Listening...")

        with source as source:
            audio = r.listen(source, phrase_time_limit=5)

    # Perform speech recognition
        try:
        # Use the default API key for Google Speech Recognition
            print("test")
            text = r.recognize_google(audio)
            print("Recognized Text:")
            pyautogui.typewrite(text)
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

        # Add your code here to perform the corresponding action for the command

    elif command == "quit":
        print("Command received: quit")
        break

# Close the client socket and server socket
client_socket.close()
server_socket.close()
