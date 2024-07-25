import nmap
import os
import sys

sys.path.append('__init__')
import get_ip as ad
import file_mg as file
import tldextract

sc = nmap.PortScanner()

def nmap():
    print("\n***************************** Welcome to the Network Scanner *****************************")
    print("********************************************************************************************")
    ip = input("\nPlease enter the IP address: ")
    sc.scan(ip, '1-1024')
    print(sc.scaninfo())
    print(sc[ip]['tcp'].keys())

    hostname = ip
    nom_fichier = f"{hostname}.txt"

    StartDate = input("\nPlease enter the start date of work : ")
    EndDate = input("\nPlease enter the end date of work : ")
    nature = input("\nPlease enter the nature of the operation : ")
    technician = input("\nPlease enter the name of the technician : ")

    ports = input("\nPlease enter the ports open : ")


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

        fichier.write("\nNature of the operation : ")
        fichier.write(nature)

        fichier.write("\nStart date of work :")
        fichier.write(StartDate)
        
        fichier.write("\nEnd date of work :")
        fichier.write(EndDate)

        fichier.write("Je soussigné ")
        fichier.write(technician)
        fichier.write(" avoir effectué l'analyse réseau au l'adresse suivant : ")
        fichier.write(ip)

        fichier.write("\rLes résultats de l'analyses sont :\r")

        fichier.write("\nThe open ports are :")
        fichier.write(ports)
    fichier.close()