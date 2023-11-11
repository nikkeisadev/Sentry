import os
import time
import psutil  
import hashlib
import secrets
import os.path
import pandas as pd
import platform  
import ctypes
import datetime
import winapps
from pathlib import Path
from winotify import Notification, audio
import tkinter
from PIL import Image, ImageTk
import customtkinter

raw_datetime = datetime.datetime.now()
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

subprefix = """
 _______                                         
(_______)        _                               
 _______ _   _ _| |_ ___   ___  ____ _____ ____  
|  ___  | | | (_   _) _ \ /___)/ ___|____ |  _ \ 
| |   | | |_| | | || |_| |___ ( (___/ ___ | | | |
|_|   |_|____/   \__)___/(___/ \____)_____|_| |_|                                                            

       <= Emptum base code for scanning =>
           Made with love, by: Nikke.

"""
print(subprefix)

installations = []
illegal_installations =['Epic', 'Discord', 'Opera']

global found
found = ''
global installation_found
installation_found = False
global switchPerm
switchPerm = True

CWD_PATH = os.getcwd()
USER_NAME = Path.home()
USERNAME_RUNTIME = platform.uname()
EMPTUM_CONSOLE_PREFIX = '[EMPTUM]> '
SPI_SETDESKWALLPAPER = 20

scanwallpaper = True
scaninstallations = True
scanstartup = True
scanruntime = True

illegal_activity = 'NO ILLEGAL ACTIVITY YET'
local_time = time.localtime()
current_time = time.strftime("%H:%M:%S", local_time)
current_date = datetime.date.today()
current_path = os.path.dirname(os.path.realpath(__file__))

if os.path.isfile(r"set_auto_scan.sv"):
    print(f"{EMPTUM_CONSOLE_PREFIX}Shared value (set_auto_scan.sv) found! EMPTUM is able to read autoscan settings!")
else:
    print(f"{EMPTUM_CONSOLE_PREFIX}Shared value (set_auto_scan.sv) NOT found! Creating one in working directory!")
    with open(r'set_auto_scan.sv', 'x') as f:
         f.write('auto_scan_mode$on\nwallpaper_protection$on\nruntime_check$on\ndirectory_scan$on\ninstallations$on\nwebblock$on')
if os.path.isfile(r"installations.hs"):
    print(f'{EMPTUM_CONSOLE_PREFIX}Installations log found! No need to generate one! Skipping...')
else:
    print(f"{EMPTUM_CONSOLE_PREFIX}Installations NOT log found! Generating a new one!")
    with open(r'installations.hs', 'x') as f:
         f.write(f'{EMPTUM_CONSOLE_PREFIX}Generated log!')

def defineApplicationKeysLoaded():
    global APPLICATION_KEYS_LOADED
    APPLICATION_KEYS_LOADED = []
    hs = open('unloaded_processes.hs', encoding='utf-8')
    for x in hs:
        d = {}
        data = x.strip().split(";")
        d["app"]=str(data[0])
        d["datetime"]=str(data[1])
        APPLICATION_KEYS_LOADED.append(d)
    hs.close()

def STANDARD_SCAN_LOOP():
    found = ''
    with open(r'scansettings.sv', 'r') as fp:
            lines = fp.readlines()
            for row in lines:
                if row.find('walloff') != -1:
                    scanwallpaper = False
                elif row.find('wallon') != -1:
                    scanwallpaper = True
                if row.find('installsoff') != -1:
                    scaninstallations = False
                elif row.find('installson') != -1:
                    scaninstallations = True
                if row.find('startoff') != -1:
                    scanstartup = False
                elif row.find('starton') != -1:
                    scanstartup = True
                if row.find('runtimeoff') != -1:
                    scanruntime = False
                if row.find('runtimeon') != -1:
                    scanruntime = True

    RUNTIME_PROCESSES = []
    global APPLICATION_KEYS_LOADED
    APPLICATION_KEYS_LOADED = []

    if scanwallpaper:
        for process in psutil.process_iter():
            RUNTIME_PROCESSES.append(process.name())
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, str(CWD_PATH) + r"\images\emptum_default_wallpaper.png" , 0)
        
    if scanruntime:
        hs = open('unloaded_processes.hs', encoding='utf-8')
        for x in hs:
            d = {}
            data = x.strip().split(";")
            d["app"]=str(data[0])
            d["datetime"]=str(data[1])
            APPLICATION_KEYS_LOADED.append(d)
        hs.close()
        noAppsFound = False
        for app_name in APPLICATION_KEYS_LOADED:
            if RUNTIME_PROCESSES.__contains__(app_name["app"]):
                with open('activity_log.hs', 'a', encoding='utf-8') as hs:
                        hs.write(f'[Activity]> Forbidden application in the system: {app_name["app"]} at {raw_datetime}!\n')
                        hs.close()
                noAppsFound = True
                print(EMPTUM_CONSOLE_PREFIX + "An Illegal process just found!")
                os.system("taskkill /f /im " + app_name["app"])
                print(EMPTUM_CONSOLE_PREFIX + "Process has been terminated!")
                illegal_activity = 'FORBIDDEN APPLICATION'
                for process in psutil.process_iter():
                    RUNTIME_PROCESSES.append(process.name())
                toast = Notification(app_id="EMPTUM - Better School Cyber Security",
                            title="Illegal activity! - " + str(current_date), 
                            msg="EMPTUM detected illegal activity in your runtime! Action reported, and logged!",
                            #duration="long",
                            icon=str(CWD_PATH) + r"\images/system_alert.ico"
                            )
                toast.set_audio(audio.Default, loop=False)
                toast.add_actions(label= app_name["app"] + " - " + illegal_activity + " - " + current_time)
                toast.show()
                with open(r'reports.txt', 'a') as f:
                    f.write(f'{app_name["app"]};{current_date}{current_time};Illegal runtime!(Auto task kill)\n')
                APPLICATION_KEYS_LOADED = []
            else:
                RUNTIME_PROCESSES = []
                app = ''
                for process in psutil.process_iter():
                    RUNTIME_PROCESSES.append(process.name())
        if noAppsFound == False:
            print(f'{EMPTUM_CONSOLE_PREFIX}No illegal processes found in runtime!')
            with open('activity_log.hs', 'a', encoding='utf-8') as hs:
                        hs.write(f'[Activity]> No forbidden application found at {raw_datetime}!\n')
                        hs.close()
    if scaninstallations:
        installation_found = False
        for app in illegal_installations:
            for item in winapps.list_installed():
                if item.name.lower().__contains__(app.lower()):
                    installations.append(item.name)
                    found = found + f'{EMPTUM_CONSOLE_PREFIX} {item.name} found, installed at: {item.install_date}!\n'
                    print(f'{EMPTUM_CONSOLE_PREFIX} {item.name} found, installed at: {item.install_date}!\n')
                    with open('installations.hs', 'a', encoding='utf-8') as f:
                        toast = Notification(app_id="EMPTUM - Better School Cyber Security",
                            title="Installation found! - " + str(current_date), 
                            msg="EMPTUM detected illegal activity in your runtime! Action reported, and logged!",
                            #duration="long",
                            icon=str(CWD_PATH) + r"\images/system_alert.ico"
                            )
                        toast.set_audio(audio.Default, loop=False)
                        toast.add_actions(label= item.name + " - " + 'Illegal Installation' + " - " + current_time)
                        toast.show()
                        f.write(found)
                        f.close()
                        installation_found = True
        if installation_found:
            print(f'{EMPTUM_CONSOLE_PREFIX}Illegal installations found! Logged into [ installations.hs ]!')
            installation_found = False
    if scanstartup:
        path = "C://Users//Nikke//AppData//Roaming//Microsoft//Windows//Start Menu//Programs//Startup//"
        ss_list = os.listdir(path)
        illegalFileInStartup = False

        print(f'{EMPTUM_CONSOLE_PREFIX}Found files in startup folder: {ss_list}\n{EMPTUM_CONSOLE_PREFIX}Start removing illegal files...')
        for file in ss_list:
            if 'desktop.ini' in file: pass
            else:
                print(f'{EMPTUM_CONSOLE_PREFIX}{file} found, deleted!') 
                illegalFileInStartup = True
                os.remove(path + file)
        if illegalFileInStartup != True: print(f'{EMPTUM_CONSOLE_PREFIX}No illegal file(s) found in Startup folder!')
while True:
     time.sleep(7)
     STANDARD_SCAN_LOOP()