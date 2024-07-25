import nmap
import os
import sys

sys.path.append('__init__')
import get_ip as ad
import file_mg as file
import tldextract

sc = nmap.PortScanner()

def vuln():
    print("\n************************* Welcome to Vulnerabilities Scanner *************************")
    print("**************************************************************************************")
    ip = input("\nPlease enter the IP address: ")
    print(os.system('nmap -sV --script=vulscan/vulscan.nse ' + ip))