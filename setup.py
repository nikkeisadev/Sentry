import os
import subprocess
import platform
import sys
import time

print('SENTRY Better School Cyber Security - nikkeisadev')

# List of required packages
required_packages = [
    'wget',
    'psutil',
    'winapps',
    'datetime',
    'customtkinter',
    'mysql-connector-python',
    'pathlib',
    'Pillow',
    'winotify',
    'colorama',
    'playsound'
]

# Install required packages
print('~ Installing required packages.')
for index, package in enumerate(required_packages):
    print(f'~ Package {index+1}/{len(required_packages)}: {package}')
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
    except subprocess.CalledProcessError as e:
        print(f'~ Error installing package: {package}. Skipping...')
        continue

import wget
# Download MySQL installer
print('~ Downloading MySQL installer.')
mysql_installer_url = 'https://dev.mysql.com/get/Downloads/MySQLInstaller/mysql-installer-web-community-8.0.28.0.msi'
mysql_installer_filename = 'mysql-installer-web-community-8.0.28.0.msi'

# Set download path
path = os.path.join(os.getcwd(), 'utils')

# Download file using wget
wget.download(mysql_installer_url, out=path)

# Open MySQL installer
print('\n~ Installing MySQL.')
if platform.system() == 'Windows':
    os.startfile(os.path.join(path, mysql_installer_filename))
else:
    print("~ MySQL installer can only be opened on a Windows machine.\nExiting...")
    time.sleep(2)
    exit()

