import platform
import ipaddress
import subprocess
import socket
import csv
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import json


def ping_ip(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", "-w", "100", str(ip)]
    try:
        subprocess.check_output(command, stderr=subprocess.DEVNULL)
        return str(ip)
    except subprocess.CalledProcessError:
        return None

def resolve_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return "inconnu"

def save_to_csv(results):
    date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"scan_{date_str}.csv"

    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Adresse IP", "Nom de l'appareil", "Date"])
        for ip, host in results:
            writer.writerow([ip, host, date_str])

    print(f"\n Résultats sauvegardés dans le fichier : {filename}")

def scan_network(network):
    print(f"Scan ICMP de la plage : {network}")
    ip_net = ipaddress.ip_network(network, strict=False)
    hosts = list(ip_net.hosts())

    results = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        for response in executor.map(ping_ip, hosts):
            if response:
                hostname = resolve_hostname(response)
                results.append((response, hostname))

    print("\nHôtes actifs détectés :\n")
    print("{:<18} {:<}".format("Adresse IP", "Nom de l'appareil"))
    print("-" * 40)
    for ip, host in results:
        print("{:<18} {}".format(ip, host))


    whitelist = charger_whitelist()

    intrus = []
    for ip, host in results:
        if ip not in whitelist:
            intrus.append((ip, host))

    if intrus:
        print("\nAppareils non autorisés détectés :")
        for ip, host in intrus:
            print(f"❌ {ip} ({host}) n’est pas dans la whitelist")
    else:
        print("\n✅ Tous les appareils détectés sont autorisés.")

    save_to_csv(results)

def charger_whitelist(nom_fichier="whitelist.json"):
    try:
        with open(nom_fichier, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Fichier de whitelist non trouvé. Aucun appareil connu.")
        return {}


#Ouvrir un terminal et taper "ipconfig" pour trouver l'adresse IP de votre machine
#Remplacer l'adresse IP par la votre
scan_network("adresse_ip") 
