import nmap

def discover_hosts(network):
	scanner=nmap.PortScanner()
	print(f"[*] scan du reseau {network}..")
	scanner.scan(hosts=network, arguments='-sn')
	hosts_actifs=[]
	for host in scanner.all_hosts():
		if scanner[host].state()=='up':
			hosts_actifs.append(host)
			print(f"[*] hote actif:{host}")
	return hosts_actifs 
