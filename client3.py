#Bencze Marton


from socket import *
import threading


port = 8080
user = socket(AF_INET, SOCK_STREAM)
user.connect(('localhost', port))

username = input('Enter your username: ')
user.send(username.encode('utf-8'))
message = user.recv(1024).decode('utf-8')
while message != 'Username is accepted!':
    print(message)
    username = input('Enter your username: ')
    user.send(username.encode('utf-8'))
    message = user.recv(1024).decode('utf-8')

print(message)
def recieve_message():
    while True:
        try:
            message = user.recv(1024).decode('utf-8')
            print(message)
        except:
            print('You left the chat!')
            user.close()
            break

def send_message():
    while True:
        text = input('')
        if text == 'quit':
            message = f'{text}'
            user.send(message.encode('utf-8'))
            user.close()
            break
        else:
            message = f'{username}: {text}'
            user.send(message.encode('utf-8'))



recieve_thread = threading.Thread(target=recieve_message)
recieve_thread.start()

#send_thread = threading.Thread(target=send_message)
#send_thread.start()
send_message()

