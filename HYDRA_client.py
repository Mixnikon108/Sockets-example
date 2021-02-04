import socket, threading, time, keyboard
#10.35.73.141
from datetime import datetime
from colorama import init, Fore, Back, Style
#10.35.73.141
#8192

init() # Iniciar colorama


def fprint(arg):
	msg = arg.split('Ç')

	if len(msg) == 1:
		msg.append(msg[0])
		msg[0] = 'SERVER'

	print(datetime.now().strftime(Style.DIM+Fore.GREEN+'[%H:%M:%S] <@'+Style.NORMAL+Fore.MAGENTA+msg[0]+Style.DIM+Fore.GREEN+'> '+Fore.WHITE+Style.BRIGHT+msg[1]))





class write(): 
	def __init__(self): 
		self.__kill = False

	def kill(self):
		self.__kill = True

	def stop(self): 
		self.__running = False

	def play(self):
		self.__running = True

	def run(self): 
		while self.__kill == False:
			if keyboard.is_pressed('c'):  # if key 'c' is pressed 
				read.stop()
				msgOUT = input(str('>> '))
				if msgOUT == '/q':
					read.kill()
					s.close()
					self.stop()
					self.kill()
					break
				s.send(msgOUT.encode())
				read.play()
			time.sleep(0.1)

		




class read(): 
	def __init__(self): 
		self.__running = True
		self.__kill = False
		  
	def stop(self): 
		self.__running = False

	def kill(self):
		self.__kill = True

	def play(self):
		self.__running = True

	def run(self): 
		l = []
		while self.__kill == False:
			time.sleep(0.5)

			try:
				msg = s.recv(2048).decode()
				l.append(msg)

				if self.__running == True:
					_ = [fprint(i) for i in l]
					l = []

			except:
				pass
			


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP, PORT = '10.35.73.141', 9999

s.connect((IP, PORT))


#Apreton de manos
USERNAME = input('Username: ')
CLAVE_PUBLICA = s.recv(2048).decode()
s.send(USERNAME.encode())


write = write()
read  = read()


l = threading.Thread(target = write.run) 
t = threading.Thread(target = read.run) 

#APRETON DE MANOS



l.start()
t.start()








