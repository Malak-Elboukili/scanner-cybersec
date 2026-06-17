# Network Vulnerability Scanner

Outil d'audit et de reconnaissance réseau automatisé développé en Python, conçu pour cartographier un réseau local, identifier les services exposés et détecter les vulnérabilités connues.

## Fonctionnalités

* 🔍 Découverte des hôtes actifs sur le réseau local.
* ⚡ Scan des ports TCP optimisé grâce au multi-threading.
* 🏷️ Banner Grabbing pour identifier les services et leurs versions.
* 🛡️ Détection des vulnérabilités connues via une base de règles JSON.
* 📊 Attribution d'un score de risque pour chaque machine analysée.
* 📄 Génération automatique de rapports d'audit en HTML.

## Technologies utilisées

* Python
* Socket Programming
* Multi-threading
* JSON
* HTML / CSS
* Git / GitHub
* Kali Linux
* Metasploitable2

## Architecture du projet

```text
scanner-cybersec/
├── modules/
│   ├── host_discovery.py
│   ├── port_scanner.py
│   ├── vuln_checker.py
│   └── report_generator.py
├── rules/
│   └── vulnerabilities.json
├── reports/
├── .gitignore
├── requirements.txt
├── README.md
└── scanner.py
```

## Environnement de test

Le projet a été testé dans un environnement virtuel isolé :

* Kali Linux
* Metasploitable2

## Exemple de fonctionnalités

* Découverte automatique des hôtes actifs.
* Détection des ports ouverts.
* Identification des services par Banner Grabbing.
* Correspondance avec des vulnérabilités connues (CVE).
* Génération d'un rapport HTML contenant les résultats de l'analyse.

## Auteur

Malak El Boukili

Étudiante Ingénieure Informatique & Réseaux – EMSI

Future Ingénieure en Cybersécurité
