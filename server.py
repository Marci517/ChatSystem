#Bencze Marton


from socket import *
import threading

port = 8080
server = socket(AF_INET, SOCK_STREAM)
server.bind(('localhost', port))
server.listen()

users = []
usernames = []


def broadcast(message, the_user=0):
    for user in users:
        if user != the_user:
            user.send(message)


def send_private(message, username, from_user):
    try:
        i = usernames.index(username)
        the_user = users[i]
        for user in users:
            if user == the_user:
                user.send(message)
                from_user.send(message)
                break
    except:
         message = 'Username not found!'
         from_user.send(message.encode('utf-8'))


def handle_user(user, address):
    while True:
        try:
            message = user.recv(1024).decode('utf-8')
            if message == 'quit':
                i = users.index(user)
                users.remove(user)
                user.close()
                username = usernames[i]
                usernames.remove(username)
                broadcast(f'{username}: Left the chat!'.encode('utf-8'))
                print(f'Disconnected with {address}')
                break

            elif message.split(' ')[1] == '/p':
                send_to_username = message.split(' ')[2]
                from_username = message.split(' ')[0]
                message = f'{from_username}{message.split(send_to_username)[1]}'
                send_private(message.encode('utf-8'), send_to_username, user)
            elif message.split(' ')[1] == '/listusers':
                user.send(f'{usernames}'.encode('utf-8'))
            else:
                broadcast(message.encode('utf-8'))
        except:
            i = users.index(user)
            users.remove(user)
            user.close()
            username = usernames[i]
            broadcast(f'{username}: Left the chat!'.encode('utf-8'))
            usernames.remove(username)
            break


def recieve_message(user, address):
    while True:
        try:
            username = user.recv(1024).decode('utf-8')

            while username in usernames:
                user.send('Username is already in use!'.encode('utf-8'))
                username = user.recv(1024).decode('utf-8')
                print(username)

            user.send('Username is accepted!'.encode('utf-8'))
            usernames.append(username)
            users.append(user)
            print(f'Username of the user is: {username}')
            broadcast(f'{username} joined the chat!'.encode('utf-8'), user)
            user.send(f'You joined the chat!'.encode('utf-8'))
            handle_user(user, address)
        except:
            break

def connection():
    while True:
        user, address = server.accept()
        print(f'Connected with {address}')
        thread = threading.Thread(target=recieve_message, args=(user, address))
        thread.start()

print('Waiting for connection...')
connection()
