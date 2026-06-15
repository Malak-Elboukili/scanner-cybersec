import os

def generate_report(results):
    html = """<!DOCTYPE html>
<html>
<head>
    <title>Rapport de Vulnerabilites</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #0e1726; color: #d3d3d3; padding: 20px; }
        .host { background-color: #152238; margin-bottom: 20px; padding: 15px; border-radius: 8px; }
        table { width: 100%; border-collapse: collapse; margin-top: 10px; }
        th, td { border: 1px solid #23395d; padding: 10px; text-align: left; }
        th { background-color: #1a2e4c; }
        .CRITIQUE { color: #ff4d4d; font-weight: bold; }
        .ELEVE { color: #ff944d; font-weight: bold; }
        .MOYEN { color: #ffcc00; font-weight: bold; }
    </style>
</head>
<body>
"""
    for host, data in results.items():
        html += f"<div class='host'><h2>Hote : {host}</h2>"
        html += """<table>
            <tr>
                <th>Port</th>
                <th>Service</th>
                <th>Version</th>
                <th>Severite</th>
                <th>Description</th>
            </tr>"""
        
        for vuln in data.get('vulns', []):
            severity_class = vuln.get('severite', 'FAIBLE')
            html += f"""<tr>
                <td>{vuln.get('port')}</td>
                <td>{vuln.get('service')}</td>
                <td>{vuln.get('version', '')}</td>
                <td><span class="{severity_class}">{severity_class}</span></td>
                <td>{vuln.get('description')}</td>
            </tr>"""
        
        html += "</table></div>"

    html += "</body>\n</html>"
    current_dir = os.path.dirname(os.path.abspath(__file__)) # Chemin du dossier 'modules'
    project_root = os.path.abspath(os.path.join(current_dir, "..")) # Remonte à 'scanner_project'
    output_path = os.path.join(project_root, "rapport.html")


    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"[*] Rapport genere avec succes a la racine : {output_path}")
