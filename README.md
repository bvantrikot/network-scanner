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
git clone https://github.com/bvantrikot/network-scanner.git
cd network-scanner
```
### 2. Trouver la bonne plage IP à scanner

Avant de lancer le script, il faut connaître ta plage IP locale (ex: `192.168.1.0/24`).
- Ouvre un terminal (cmd ou PowerShell) et tape :
```bash
ipconfig
```
- Trouver l'adresse IPv4 souvent sous cette forme :

# Exemple : 
```bash
   Adresse IPv4. . . . . . . . . . . . . .: 192.168.1.1
   Masque de sous-réseau. . . . . . . . . : 255.255.255.0
```
Grâce au masque de sous-réseau, on peut determiner la plage 
Le masque `255.255.255.0` correspond à une notation CIDR de `/24`, ce qui veut dire :

Les 24 premiers bits identifient le réseau
Les 8 derniers bits sont disponibles pour les hôtes (car 32 - 24 = 8)

- Déterminer l'adresse du réseau : 
L’adresse du réseau est obtenue en mettant tous les bits des hôtes à 0.

Dans notre exemple :

- Adresse IP : `192.168.1.1`
- Masque : `255.255.255.0` → soit `/24`

Avec un `/24`, il y a `2^8 = 256` adresses possibles (de 0 à 255 en dernier octet sauf pour `192.168.1.0` est l’adresse du réseau (non attribuable) et `192.168.1.0` est l’adresse du réseau qui est non attribuable)

Donc l’adresse du réseau est : `192.168.1.0/24` (à mettre dans le fichier python 

