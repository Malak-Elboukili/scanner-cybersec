import json 
 
def check_vulns(ports):
	with open('rules/vulnerabilities.json','r') as f :
		rules=json.load(f)['rules']
	vulns=[]
	for port_info in ports:
		for rule in rules:
			if int(port_info['port'])==rule['port']:
				vulns.append({
					'port':port_info['port'],
					'service':port_info['name'],
					'version':port_info['version'],
					'severity':rule['severity'],
					'description':rule['description']
					})

				print(f"[!]{rule['severity']}-port{port_info['port']}-{rule['description']}")
	return vulns
