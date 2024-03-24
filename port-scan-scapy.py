from scapy.all import *
conf.verb = 0 #configura o modo verbose 0, deixando a saida do scapy mais limpa
portas = [21,22,80,23,8080,445]
pacoteIP = IP(dst="IP do destino")
pacoteTCP = TCP(dport=portas, flags="S")
pacote = pacoteIP/pacoteTCP
ans, unans = sr(pacote, inter=0.1, timeout=1) #envia pacote tcp/ip com a flag syn e aguarda por resposta
print ("Porta\tEstado")
for pacoteRecbido in ans:
	print (pacoteRecebido[1][IP].sport, \
	"\t", pacoteRecebido[1][TCP].sprintf("%flags%")) #exibe qual a porta de origem do pacote-resposta
