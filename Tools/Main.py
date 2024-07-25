#!usr/bin/python3
#pip3 install python-nmap
#pip install --upgrade termcolor
#pip install art 
#git clone https://github.com/scipag/vulscan.git -> mv in C:\Program Files (x86)\Nmap\scripts
#pip install tldextract

import nmap
import os
import sys
from art import *
from termcolor import colored
import tldextract
from hashlib import sha256

import ScanNetwork
import VulnScanner
import Cryptage
import Analyse


sys.path.append('__init__')
import get_ip as ad
import file_mg as file

sc = nmap.PortScanner()

print(colored("""
_______    .-------.     .-./`)  .-./`)  .-./`)      ,-----.         _______    .---.  .---.      .-''-.       .-''-.   
\  ____  \  |  _ _   \    \ .-.') \ .-.') \ .-.')   .'  .-,  '.      /   __  \   |   |  |_ _|    .'_ _   \    .'_ _   \  
| |    \ |  | ( ' )  |    / `-' \ / `-' \ / `-' \  / ,-.|  \ _ \    | ,_/  \__)  |   |  ( ' )   / ( ` )   '  / ( ` )   ' 
| |____/ /  |(_ o _) /     `-'`"`  `-'`"`  `-'`"` ;  \  '_ /  | : ,-./  )        |   '-(_{;}_) . (_ o _)  | . (_ o _)  | 
|   _ _ '.  | (_,_).' __   .---.   .---.   .---.  |  _`,/ \ _/  | \  '_ '`)      |      (_,_)  |  (_,_)___| |  (_,_)___| 
|  ( ' )  \ |  |\ \  |  |  |   |   |   |   |   |  : (  '\_/ \   ;  > (_)  )  __  | _ _--.   |  '  \   .---. '  \   .---. 
| (_{;}_) | |  | \ `'   /  |   |   |   |   |   |   \ `"/  \  ) /  (  .  .-'_/  ) |( ' ) |   |   \  `-'    /  \  `-'    / 
|  (_,_)  / |  |  \    /   |   |   |   |   |   |    '. \_/``".'    `-'`-'     /  (_{;}_)|   |    \       /    \       /  
/_______.'  ''-'   `'-'    '---'   '---'   '---'      '-----'        `._____.'   '(_,_) '---'     `'-..-'      `'-..-'   
                                                                                                                         """, 'red'))

# print(colored(text2art('Created-by-Briiiochee\n\n'), 'cyan'))
print(colored('Created-by-Briiiochee\n\n', 'cyan'))


def main(): 
    n = input("1. Network scanner\n2. Vulnerabilities Detection\n3. Exploit\n4. Cryptage\n5. Analyse \n\nPlease enter the number : ")

    if n == '1':
        ScanNetwork.nmap()
    elif n == '2':
        VulnScanner.vuln()
    elif n == '3':
        os.system('msfconsole')
    elif n == '4':
        Cryptage.crypt()
    elif n == '5':
        Analyse.analyse()   
    else:
        print("Please choose the number between 1 and 5")

if __name__=="__main__":
    main()