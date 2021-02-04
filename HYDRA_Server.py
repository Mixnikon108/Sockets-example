import socket, keyboard, threading, time
from datetime import datetime
from colorama import init, Fore, Back, Style
#10.35.73.141
#8192

init() # Iniciar colorama

def fprint(msg):
	print(datetime.now().strftime(Style.DIM+Fore.GREEN+'[%H:%M:%S] '+Fore.WHITE+Style.BRIGHT+msg))


def sendALL(message):
	for clients in list_of_clients:
		clients.send(message.encode())


def CommIN(client):
	global list_of_clients

	txt = '¡Esto es una clave publica!'
	client.send(txt.encode()) #Mandamos la clave publica
	Client_username = client.recv(1024).decode() #Recibimos el nombre de usuario encriptado
	sendALL('Se ha unido '+ Client_username)

	while True:
		try:
			msg = client.recv(1024).decode()
			msg = Client_username + 'Ç' + msg
			sendALL(msg)
		except:
			del list_of_clients[list_of_clients.index(client)]
			client.close()
			sendALL(Client_username+ ' se ha desconectado')
			fprint('User {} has disconnected.'.format(address))
			fprint('Currently active connections: {}/{}'.format(len(list_of_clients), QUEUE))
			break

			


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Iniciar la libreria

IP, PORT , QUEUE = '10.35.73.141', 9999, 5




s.bind((IP, PORT)) #Abrir socket

s.listen(QUEUE) #Abrir queue de escucha


list_of_clients = []


print(Style.RESET_ALL + 'IP: '        + Fore.RED + str(IP))
print(Style.RESET_ALL + 'PORT:'       + Fore.RED + str(PORT))

print("Server has been initiated correctly and it's ready to deploy.")



print(Style.RESET_ALL + 		      'Main details overview:')
print(Style.RESET_ALL + Fore.YELLOW + '______________________________________________')
print(Style.RESET_ALL + Fore.YELLOW + '█											█')
print(Style.RESET_ALL + Fore.YELLOW + '█			INICIATED AS SERVER				█')
print(Style.RESET_ALL + Fore.YELLOW + '█____________________________________________█')
print(Style.RESET_ALL + Fore.YELLOW + '█_________IP__________|________{}			  '.format(IP))
print(Style.RESET_ALL + Fore.YELLOW + '█________PORT_________|________{}			  '.format(PORT))
print(Style.RESET_ALL + Fore.YELLOW + '█_______QUEUE_________|________{}			  '.format(QUEUE))
print(Style.RESET_ALL + Fore.YELLOW + '█____BUFFER_SIZE______|________{}			  '.format('1024'))
print(Style.RESET_ALL + Fore.YELLOW + '█_______STATUS________|________ONLINE________█')

print('\n\n')
fprint('Now listenig...')








while True:
	if len(list_of_clients) <= QUEUE:
		client, address = s.accept()

		fprint('User {} has connected.'.format(address))
		list_of_clients.append(client)
		fprint('Currently active connections: {}/{}'.format(len(list_of_clients), QUEUE))


		threading.Thread(target=CommIN, args=(client,)).start()

	
