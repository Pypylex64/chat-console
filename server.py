import socket
import colorama
from datetime import datetime
from colorama import Fore, Style

colorama.init()
clients = []

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('255.255.255.0', 11719))                        # через ipconfig, IPv4

quit = False
print("[Server Started]")

while not quit:
	try:
		data, addr = s.recvfrom(1024)

		if addr not in clients:
			clients.append(addr)
			for client in clients:
                time.sleep(0.2)
				s.sendto(('На сервере '+str(len(clients)) + '/200 человек').encode("utf-8"),client)

		server_time = datetime.strftime(datetime.now(), "%Y-%m-%d-%H.%M.%S")

		print("["+addr[0]+"]=["+str(addr[1])+"]=["+server_time+"]/",end="")
		print(data.decode("utf-8"))

		for client in clients:
			if addr != client:
				s.sendto(data,client)
	except:
		print("\n[Server Stopped]")
		quit = True

s.close()
