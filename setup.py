import os
import subprocess
import platform
import sys
import urllib.request
import time

# List of required packages
required_packages = [
    'psutil',
    'winapps',
    'datetime',
    'customtkinter',
    'mysql-connector-python',
    'pathlib',
    'Pillow',
    'winotify',
    'colorama'
]

# Install required packages
print('Installing required packages.\nIF THE INSTALLER STOPPED, PLEASE PRESS ENTER TO CONTINUE TO OTHER PACKAGES!!!')
for index, package in enumerate(required_packages):
    print(f'Package {index+1}/{len(required_packages)}: {package}')
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
    except subprocess.CalledProcessError as e:
        print(f'Error installing package: {package}. Skipping...')
        continue
    # Download MySQL installer
print('Downloading MySQL installer.')
mysql_installer_url = 'https://dev.mysql.com/get/Downloads/MySQLInstaller/mysql-installer-web-community-8.0.28.0.msi'
mysql_installer_filename = 'mysql-installer.msi'

urllib.request.urlretrieve(mysql_installer_url, mysql_installer_filename)

# Open MySQL installer
print('Installing MySQL.')
if platform.system() == 'Windows':
    os.startfile(mysql_installer_filename)
else:
    print("MySQL installer can only be opened on a Windows machine.\nExiting...")
    time.sleep(1)
    exit()