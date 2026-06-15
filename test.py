from modules.host_discovery import discover_hosts
from modules.port_scanner import scan_ports
from modules.vuln_checker import check_vulns 
hosts=discover_hosts('192.168.0.0/24')
for host in hosts:
	ports=scan_ports(host)
	vulns=check_vulns(ports)
