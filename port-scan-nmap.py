import nmap
scanNmap = nmap.PortScanner()
scanNmap.scan("host", "21,80")
print scanNmap.commandline()
for host in scanNmap.all_hosts():
	print "Nmap scan report for", host
	print "Host is", scanNmap[host]["status"]["state"]
	for protocolo in scanNmap[host].all_protocols():
		print "PORT\tSTATE\tSERVICE"
		for porta in scanNmap[host][protocolo]:
			alvo = scanNmap[host][protocolo][porta]
			print str(porta) + "/" + protocolo + "\t" + \
			alvo["state"] + "\t" + alvo["name"]
	MAC = scanNmap[host]["addresses"]["mac"]
	print "MAC Address: " + MAC + "(" + \
	scanNmap[host]["vendor"][MAC] + ")" + "\n"
