import os
import time
import psutil  
import os.path
import platform  
import ctypes
import datetime
import winapps
from pathlib import Path
from winotify import Notification, audio
import colorama
from colorama import Fore
import mysql.connector

INSTALLATIONS_INJECTS = []
APPLICATION_INJECTS = []
illegal_installations = []
raw_datetime = datetime.datetime.now()
installations = []
installations =[]

global found
found = ''
global installation_found
installation_found = False
global switchPerm
switchPerm = True

CWD_PATH = os.getcwd()
USER_NAME = Path.home()
USERNAME_RUNTIME = platform.uname()
SENTRY_CONSOLE_PREFIX = f'{Fore.MAGENTA}[{Fore.WHITE}SENTRY{Fore.MAGENTA}]{Fore.WHITE}> '
SPI_SETDESKWALLPAPER = 20

scanwallpaper = True
scaninstallations = True
scanstartup = True
scanruntime = True

illegal_activity = 'NO BLACKLISTED ACTIVITY YET'
local_time = time.localtime()
current_time = time.strftime("%H:%M:%S", local_time)
current_date = datetime.date.today()
current_path = os.path.dirname(os.path.realpath(__file__))

def getSQLKey(path):
    with open(path, 'r') as file:
        password = file.readline().strip()
    return password

keypath = 'sql/key/sql.key'
key = getSQLKey(keypath)

def connectSQL(key):
    global init_success
    init_success = False
    mydb = mysql.connector.connect(
    host = "127.0.0.1",
    port = 8080,
    user = "root",
    password = key,
    database = "token_storage"
    )
    mycursor = mydb.cursor()

    if mydb.is_connected:
        init_success = True
        pass
    else:
        init_success = False
        time.sleep(2)

#Connecting to the backend.
#The key is stored in a file, called as sql.key.
connectSQL(key)

def reportToSQLDatabase(aboutReport, aboutDatetime, aboutID, aboutInforamtion):
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        port=8080,
        user="root",
        password=SQLPASSWORD,
        database="token_storage"
    )

    sql = "INSERT INTO report_table (about, datetime, id, information) VALUES (%s, %s, %s, %s)"
    val = (aboutReport, aboutDatetime, aboutID, aboutInforamtion)
    
    mycursor = mydb.cursor()
    mycursor.execute(sql, val)
    mydb.commit()

def injectInstallations(self):
        self.INSTALLATIONS_INJECTS = []
        hs = open('installations.hs', encoding='utf-8')
        try:
            for x in hs:
                d = {}
                data = x.strip().split(";")
                d["app"]=str(data[0])
                d["datetime"]=str(data[1])
                self.INSTALLATIONS_INJECTS.append(d)
            hs.close()
        except FileNotFoundError:
            self.injectInstallations()

def injectApplications(self):
    self.APPLICATION_INJECTS = []
    hs = open('unloaded_processes.hs', encoding='utf-8')
    try:
        for x in hs:
            d = {}
            data = x.strip().split(";")
            d["app"]=str(data[0])
            d["datetime"]=str(data[1])
            self.APPLICATION_INJECTS.append(d)
        hs.close()
    except FileNotFoundError:
        self.injectApplications()

if os.path.isfile(r"set_auto_scan.sv"):
    print(f"{SENTRY_CONSOLE_PREFIX}Shared value (set_auto_scan.sv) found! SENTRY is able to read autoscan settings!")
else:
    print(f"{SENTRY_CONSOLE_PREFIX}Shared value (set_auto_scan.sv) NOT found! Creating one in working directory!")
    with open(r'set_auto_scan.sv', 'x') as f:
         f.write('auto_scan_mode$on\nwallpaper_protection$on\nruntime_check$on\ndirectory_scan$on\ninstallations$on\nwebblock$on')
if os.path.isfile(r"installations.hs"):
    print(f'{SENTRY_CONSOLE_PREFIX}Installations log found! No need to generate one! Skipping...')
else:
    print(f"{SENTRY_CONSOLE_PREFIX}Installations NOT log found! Generating a new one!")
    with open(r'installations.hs', 'x') as f:
         f.write(f'{SENTRY_CONSOLE_PREFIX}Generated log!')

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
    global scanruntime
    global scaninstallations
    global scanwallpaper
    global scanstartup
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
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, str(CWD_PATH) + r"/images/sentry_default_wallpaper.png" , 0)
        
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
                print(SENTRY_CONSOLE_PREFIX + f"{Fore.YELLOW}A Blacklisted process just found!")
                os.system("taskkill /f /im " + app_name["app"])
                print(SENTRY_CONSOLE_PREFIX + f"{Fore.GREEN}Process has been terminated!")
                illegal_activity = 'FORBIDDEN APPLICATION'
                for process in psutil.process_iter():
                    RUNTIME_PROCESSES.append(process.name())
                toast = Notification(app_id="SENTRY - Better School Cyber Security",
                            title="Blacklisted activity! - " + str(current_date), 
                            msg="SENTRY detected Blacklisted activity in your runtime! Action reported, and logged!",
                            #duration="long",
                            icon=str(CWD_PATH) + r"\images/system_alert.ico"
                            )
                toast.set_audio(audio.Default, loop=False)
                toast.add_actions(label= app_name["app"] + " - " + illegal_activity + " - " + current_time)
                toast.show()
                reportToSQLDatabase(f'[auto-runtime]', f'{current_date} {current_time}', MACHINE_ID, 'Blacklisted runtime application!')
                with open(r'reports.txt', 'a') as f:
                    f.write(f'{app_name["app"]};{current_date}{current_time};Blacklisted runtime!(Auto task kill)\n')
                APPLICATION_KEYS_LOADED = []
            else:
                RUNTIME_PROCESSES = []
                app = ''
                for process in psutil.process_iter():
                    RUNTIME_PROCESSES.append(process.name())
        if noAppsFound == False:
            print(f'{SENTRY_CONSOLE_PREFIX}No Blacklisted processes found in runtime!')
            pass

    if scaninstallations:
        installation_found = False
        for app in illegal_installations:
            for item in winapps.list_installed():
                if item.name.lower().__contains__(app.lower()):
                    installations.append(item.name)
                    found = found + f'{SENTRY_CONSOLE_PREFIX} {item.name} found, installed at: {item.install_date}!\n'
                    print(f'{SENTRY_CONSOLE_PREFIX} {Fore.MAGENTA}{item.name}{Fore.YELLOW} found, installed at: {item.install_date}!\n')
                    with open('installations.hs', 'a', encoding='utf-8') as f:
                        toast = Notification(app_id="EMPTUM - Better School Cyber Security",
                            title="Installation found! - " + str(current_date), 
                            msg="EMPTUM detected Blacklisted activity in your runtime! Action reported, and logged!",
                            #duration="long",
                            icon=str(CWD_PATH) + r"\images/system_alert.ico"
                            )
                        toast.set_audio(audio.Default, loop=False)
                        toast.add_actions(label= item.name + " - " + 'Blacklisted Installation' + " - " + current_time)
                        toast.show()
                        f.write(found)
                        f.close()
                        with open(r'reports.txt', 'a') as f:
                            f.write(f'{item.name};{current_date}{current_time};Blacklisted installation\n')
                        installation_found = True
        if installation_found:
            print(f'{SENTRY_CONSOLE_PREFIX}Blacklisted installations found! Logged into [ installations.hs ]!')
            installation_found = False
            reportToSQLDatabase(f'[auto-installation]', f'{current_date} {current_time}', MACHINE_ID, 'Blacklisted installation found!')
    if scanstartup:
        path = f'C://Users//{os.getenv("USERNAME")}//AppData//Roaming//Microsoft//Windows//Start Menu//Programs//Startup//'
        ss_list = os.listdir(path)
        illegalFileInStartup = False

        print(f'{SENTRY_CONSOLE_PREFIX}Found files in startup folder: {Fore.MAGENTA}{ss_list}')
        for file in ss_list:
            if 'desktop.ini' in file: pass
            else:
                print(f'{SENTRY_CONSOLE_PREFIX}{Fore.YELLOW}{file} found, deleted!') 
                illegalFileInStartup = True
                os.remove(path + file)
                reportToSQLDatabase(f'[auto-start-up]', f'{current_date} {current_time}', MACHINE_ID, f'Blacklisted file found in startup folder! [{file}]')
                with open(r'reports.txt', 'a') as f:
                    f.write(f'{file};{current_date}{current_time};Blacklisted file in startup\n')
        if illegalFileInStartup != True: print(f'{SENTRY_CONSOLE_PREFIX}No illegal file(s) found in Startup folder!')
while True:
     time.sleep(1)
     STANDARD_SCAN_LOOP()
