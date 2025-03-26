# Network Scanner – Détection d'appareils sur le réseau local 

Ce mini projet Python permet de scanner un réseau local (Wi-Fi ou Ethernet) pour détecter tous les appareils actifs et identifier ceux qui ne sont pas autorisés selon une whitelist défini manuellement

## Fonctionnalités

-  Scan ICMP d'une plage IP 
-  Résolution des noms des machines (reverse DNS)
-  Export automatique en `.csv` avec horodatage
-  Détection des intrus via une `whitelist.json`
-  Aucune dépendance externe : tout est en Python natif

## 🛠️ Utilisation

### 1. Cloner le repo
```bash
git clone https://github.com/ton-utilisateur/network-scanner.git
cd network-scanner
