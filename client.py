# Event-Driven Programming
# # Here we're creating the client Script that connects to the Server

import socket, threading

DISCONNECT_MESSAGE ="!DISCONNECT!"
HEADER = 2048

SERVER_HOST = '5.62.147.20' # socket.gethostbyname('3c9b5f55-fd2c-4cbd-885d-ffb7dcc82cd4.api.beta.kintohub.com/htica-server/')
SERVER_PORT = 5050
SERVER_ADDR = (SERVER_HOST, SERVER_PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(SERVER_ADDR)

print(f"[CLIENT] CONNECTED TO THE SERVER: {SERVER_ADDR[0]}:{SERVER_ADDR[1]}")

def send(msg, sender_name):
	sender_name = str.encode(sender_name)
	client.send(sender_name)
	message = str.encode(msg)
	client.send(message)

def get_messages(sender, are_you_sure):
	if are_you_sure:
		new_message = client.recv(HEADER).decode()
		if new_message.startswith('[{sender}]'):
			pass
		else:
			print("\n" + new_message)
	else:
		pass

sender = input('Enter your Name: ')

print(f'\n[CLIENT] to disconnect enter "{DISCONNECT_MESSAGE}" (without quotes)\n')

while True:
	message = input(f"{sender}> ")
	if message.strip() == "":
		threading.Thread(target=get_messages, args=(sender, True)).start()
	else:
		if message == DISCONNECT_MESSAGE:
			send(message, sender)
			print(f"[CLIENT] DISCONNECTED to the SERVER {SERVER_ADDR}")
			exit()
		else:
			send(message, sender)
