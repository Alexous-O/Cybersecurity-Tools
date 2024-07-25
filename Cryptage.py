import nmap
import os
import sys
from art import *
from termcolor import colored
import tldextract
from hashlib import sha256

def crypt():
    print("\n***************************** Welcome to the Cryptography *****************************")
    print("***************************************************************************************")
    entree = input("\nEnter the name of the file to encrypt/decrypt : ")
    sortie = input("Enter from output file : ")
    key = input("Enter the encryption key : ")
    keys = sha256(key.encode('utf-8')).digest()
    with open(entree, 'rb') as f_entree:
        with open(sortie, 'wb') as f_sortie:
            i = 0   
            while f_entree.peek():
                c = ord(f_entree.read(1))
                j = i % len(keys)
                b = bytes([c^keys[j]])
                f_sortie.write(b)
                i = i + 1