from scapy.all import *
conf.verb = 0
host = input("Digite o ip do destino: ")
portas = [22,80,666,8080,21]
pacote = IP(dst=host) / TCP(dport=portas, flags="S")
ans, unans = sr(pacote, inter =0.1, timeout=1)
print ("PORTA\tESTADO")
for pacoteRecebido in ans:
	if pacoteRecebido[1].haslayer("ICMP"):
		if pacoteRecebido[1]["ICMP"].type == 3 \
		and pacoteRecebido[1]["ICMP"].code == 3 :
			print (pacoteRecebido[0][TCP].dport , "\tREJECT")
	elif pacoteRecebido[1].haslayer("TCP")
		print (pacoteRecebido[1][TCP].sport, "\t", \)
		pacoteRecebido[1][TCP].sprintf("%flags%")
for pacoteNaoRecebido in unans:
	print (pacoteNaoRecebido.dport, "\tDROP")
