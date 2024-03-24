import socket
host = input("Digite o host: ")
portas = [21,22,80,80080,445]
print ("Portas Abertas")
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(1)
	codigoRetorno = sock.connect_ex((host, porta))
	sock.close()
	if codigoRetorno == 0;
		print (porta)
