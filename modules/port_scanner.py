import nmap 
def scan_ports(host):
	scanner=nmap.PortScanner()
	print(f"[*] scan des ports de {host}..")
	scanner.scan(host,arguments=' --open')
	ports=[]
	if host in scanner.all_hosts():
		for proto in scanner[host].all_protocols():
			for port in scanner[host][proto].keys():
				service=scanner[host][proto][port]
				ports.append({
					'port':port,
					'protocol':proto,
					'state':service['state'],
					'name':service['name'],
					'version':service['version']
				})
				print(f"[*] prot {port}/{proto}-{service['name']}{service['version']}")
	return ports 
