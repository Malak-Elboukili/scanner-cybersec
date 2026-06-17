# Network Vulnerability Scanner

Scanner de vulnérabilités réseau développé en Python permettant d'automatiser la découverte des hôtes actifs, le scan des ports TCP et l'identification des vulnérabilités potentielles.

## Fonctionnalités

- Découverte des hôtes actifs sur le réseau
- Scan des ports TCP
- Multi-threading pour améliorer les performances
- Banner Grabbing pour identifier les services
- Détection des vulnérabilités à partir d'une base de règles JSON
- Attribution d'un score de risque par machine
- Génération automatique de rapports HTML

## Technologies utilisées

- Python
- Socket Programming
- Threading
- JSON
- HTML/CSS
- Git / GitHub
- Kali Linux
- Metasploitable2

## Environnement de test

Le projet a été testé dans un environnement virtuel isolé :

- Kali Linux
- Metasploitable2

## Structure du projet

```
scanner-cybersec/
│
├── scanner.py
├── rules.json
├── requirements.txt
├── reports/
├── screenshots/
└── README.md
```

## Exemple de détection

Le scanner permet :

- d'identifier les ports ouverts ;
- de récupérer les bannières des services ;
- d'associer certaines signatures à des vulnérabilités connues ;
- de générer un rapport HTML contenant les résultats de l'analyse.

## Auteur

Malak El Boukili

Étudiante Ingénieure Informatique & Réseaux – EMSI

Intérêt particulier pour la cybersécurité et les systèmes Linux.
