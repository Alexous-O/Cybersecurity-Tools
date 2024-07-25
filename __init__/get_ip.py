# Récupéré adresse IP à traver une URL
import socket
import sys
import tldextract

def get(url):
    hostname = url
    print('Création du fichier en cours...')
    extracted_info = tldextract.extract(url)
    print("\nThe result :", extracted_info)
    print("\nThe hostnane :", extracted_info.domain)

    hostname = extracted_info.domain
    nom_fichier = f"{hostname}.txt"

    ip = socket.gethostbyname(url)
    
    with open("reports/" + nom_fichier, 'w', encoding="utf-16") as fichier:
       
        fichier.write("""
 _____                                           _           _   _                                       _     _                 
|  __ \                                         | |         | | ( )                                     | |   (_)                
| |__) |   __ _   _ __    _ __     ___    _ __  | |_      __| | |/    ___  __  __   ___    ___   _   _  | |_   _    ___    _ __  
|  _  /   / _` | | '_ \  | '_ \   / _ \  | '__| | __|    / _` |      / _ \ \ \/ /  / _ \  / __| | | | | | __| | |  / _ \  | '_ \ 
| | \ \  | (_| | | |_) | | |_) | | (_) | | |    | |_    | (_| |     |  __/  >  <  |  __/ | (__  | |_| | | |_  | | | (_) | | | | |
|_|  \_\  \__,_| | .__/  | .__/   \___/  |_|     \__|    \__,_|      \___| /_/\_\  \___|  \___|  \__,_|  \__| |_|  \___/  |_| |_|
                 | |     | |                                                                                                     
                 |_|     |_|                                                                                                     """)
        fichier.write("\n\n----------------------------------------------------------------------------------------------------------------------------------\r")
        fichier.write("\nLe rapport final d’exécution, dont le format est libre, vise à faire état des actions menées, des résultats constatés et des \nretombées obtenues du projet :\r")
        fichier.write("\nThe URL : ")
        fichier.write(hostname)
        fichier.write("\nThe IP Adresse : ")
        fichier.write(ip)
    fichier.close()
    return ip, hostname



    
