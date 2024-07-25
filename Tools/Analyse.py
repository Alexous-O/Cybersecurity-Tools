import nmap
import os
import sys

import get_ip as ad

from art import *
from termcolor import colored
import tldextract
from hashlib import sha256


def analyse():
    print("\n****************************** Welcome to the Analyse ******************************")
    print("**************************************************************************************")
    url = input("Please enter the url (ex: www.google.com) : ")
    extracted_info = tldextract.extract(url)
    hostname = extracted_info.domain

    # path_dir = "reports/" + hostname
    # file.create_dir(path_dir)
    ip = ad.get(url)
    print('\nThe IP Address is : ', ip)

    # os.system('gnome-terminal -- bash -c "nmap -A '+ip+' -o '+path_dir+'/nmap.txt && bash"') # Connaitre les services qui y tournent et les ports ouverts
    # os.system('gnome-terminal -- bash -c "nikto +h'+url+' -output '+path_dir+'/nikto.txt && bash"') # Scanning sur l'application web pour connaitre et detecter les vulnérabilitées 
    # os.system('gnome-terminal -- bash -c "python3 __init__/dirsearch/dirsearch.py -u ' +url + '-e * --simple-report='+path_dir+'/dirsearch.txt && bash"')
