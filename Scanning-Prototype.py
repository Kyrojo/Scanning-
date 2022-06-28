

import socket
import termcolor


def scan(target, ports):
	print('\n' + ' Memulai Scaning ' + '\t'+ str(target))
	for port in range(1,ports):
		scan_port(target,port)


def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print("[+] Port Opened " + str(port))
		sock.close()
	except:
		pass


targets = input("[*] Masukan Target Untuk Scan: ")
ports = int(input("[*] Mau Berapa Banyak : "))
if ',' in targets:
	print(termcolor.colored(("[*] Scan beberapa target"), 'green'))
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets,ports)
