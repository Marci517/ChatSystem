
# Python Socket Chat Application

This project is a terminal-based chat application developed in Python using the `socket` and `threading` modules. It supports multiple clients connected to a central server, where users can send public messages to all users or private messages to specific users.

## Features

- Real-time messaging between multiple clients
- Broadcasting public messages to all connected users
- Sending private messages to specific users
- Listing currently connected usernames
- Graceful disconnection using the `quit` command
- Username uniqueness check on login

## File Structure

- `server.py` – The main server script that handles client connections and message routing
- `client.py` – The client script that connects to the server and provides an interface for communication

## How to Run

### 1. Start the server

Run the following command in a terminal window:

python server.py


Expected output:

Waiting for connection...


### 2. Start a client

Open another terminal window and run:

python client.py


You will be prompted to enter a username. If the username is already in use, the server will ask for another one.

## Commands

- To send a public message:  
  Simply type your message and press Enter.

- To send a private message:  
  Use the following format:

/p <recipient_username> <message>


Example:

/p bob Hello Bob!


- To list all connected users:

/listusers


- To exit the chat:

quit


## Requirements

- Python 3.x
- No third-party libraries are required

## Notes

- The server must be started before any clients are connected.
- Communication is handled locally via `localhost` on port `8080`.
- The server automatically notifies all users when someone joins or leaves the chat.

## Example Session

Enter your username: alice Username is accepted! You joined the chat! bob joined the chat! bob: Hello everyone! alice /p bob Hi Bob, this is a private message.


## Possible Improvements

- Add timestamps to messages
- Introduce a graphical user interface (GUI)
- Support for saving chat history to a file
- Implement file sharing between users



