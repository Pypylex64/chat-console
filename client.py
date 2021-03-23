# -*- coding: utf-8 -*-

import threading
import socket
import time
import random
import colorama
from colorama import Fore, Style

colorama.init()

def receving (name, sock, switch):
	'''
	Сбор сообщений
	'''
	while not switch:
		try:
			while True:
				data, addr = sock.recvfrom(1024)
				print('\n'+data.decode("utf-8"))
				time.sleep(0.2)
		except:
			pass


shutdown = False
join = False

host = socket.gethostbyname(socket.gethostname())
port = 0

server = ("255.255.255.0", 11719)          # через ipconfig, IPv4

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

colors = [Fore.CYAN, Fore.MAGENTA, Fore.GREEN, Fore.RED]

name = input("$ name: ")
name = list(name)
name = [random.choice(colors) + char + Fore.RESET for char in name]
name = ''.join(name)

s.sendto((str("["+name+"] => join chat ")).encode("utf-8"), server)
time.sleep(0.2)

rT = threading.Thread(target = receving, args = ("RecvThread", s, shutdown))
rT.start()

# отправка сообщений 
while shutdown == False:
	try:
		print("["+name+"] > ", end='')
		print(Fore.GREEN, end='')
		message = input()
		message = Fore.GREEN+message+Fore.RESET
		print(Fore.RESET, end='')
		
		if message != "":
			 s.sendto(("["+name+"] > "+message).encode("utf-8"), server)
		time.sleep(0.2)
		
	except:
		s.sendto(("["+name+"] <= left chat ").encode("utf-8"), server)
		shutdown = True

rT.join()
s.close()
