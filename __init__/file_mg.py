# File Management va permettre de créer le répertoir pour stocker les rapports 
import os 

def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' created successfully.")

def write_file(path,data):
    file = open(path, 'w')
    file.write(data)
    file.close()