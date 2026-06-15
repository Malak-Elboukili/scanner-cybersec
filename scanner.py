from modules.host_discovery import discover_hosts
from modules.port_scanner import scan_ports
from modules.vuln_checker import check_vulns
from modules.report_generator import generate_report

network = '192.168.0.0/24'
results = {}

hosts = discover_hosts(network)
for host in hosts:
    ports = scan_ports(host)
    vulns = check_vulns(ports)
    results[host] = {'ports': ports, 'vulns': vulns}

generate_report(results)
