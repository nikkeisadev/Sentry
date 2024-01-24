import ctypes,os,threading,time,psutil,winapps,hashlib,os.path,datetime,platform,subprocess,customtkinter,mysql.connector,sys
from pathlib import Path
from PIL import Image, ImageTk
from winotify import Notification, audio
from colorama import init, Fore
from playsound import playsound

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

idList = []
installations = []
sentRequest = False
installation_found = False
init_success = False
switchPerm = True
found = ''

raw_datetime = datetime.datetime.now
local_time = time.localtime()
current_time = time.strftime("%H:%M:%S", local_time)
current_date = datetime.date.today()
current_path = os.path.dirname(os.path.realpath(__file__))
home_directory = os.path.expanduser( '~' )
scriptDir = os.path.dirname(os.path.realpath(__file__))
soundFile = (scriptDir + os.path.sep + '/sounds/click.wav')

CWD_PATH = os.getcwd()
USER_NAME = Path.home()
USERNAME_RUNTIME = platform.uname()
EMPTUM_CONSOLE_PREFIX = f'{Fore.MAGENTA}[{Fore.WHITE}SENTRY{Fore.MAGENTA}]{Fore.WHITE}> '
SPI_SETDESKWALLPAPER = 20
MACHINE_ID = None

# SQL ADMINISTRATOR PASSWORD
def getSQLKey(path):
    with open(path, 'r') as file:
        password = file.readline().strip()
    return password

keypath = 'sql/key/sql.key'
SQLPASSWORD = getSQLKey(keypath)


print(f"""{Fore.MAGENTA}
                                                                                                                              
                                                                                                                                                                                                                                         
                @@@@@@@@@@                                                                                                    
             @@@@@@@@@@@@@@@@                                                                                                 
            @@@@@@@@@@@@@@@@@@                                                                                                
           @@@@@@@@@@@@@@@@@@@@         @@@@@@@@@@@  @@@@@@@@@@@@ @@@@     @@@ @@@@@@@@@@@@@@@@@@@@@@@@   @@@     @@@@        
          @@@@@@@@@@@@@@@@@@@@@@       @@@@                       @@@@@@   @@@      @@@              @@@   @@@   @@@@         
     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@@@@@@@@  @@@@@@@@@@@@ @@@@@@@@ @@@      @@@     @@@@@@@@@@@@    @@@@@@@@          
     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          @@@@              @@@@  @@@@@@      @@@     @@@@@@@@@@        @@@@            
          @@@@@@@@@@@@@@@@@@@@@@        @@@@@@@@@@@  @@@@@@@@@@@@ @@@     @@@@      @@@     @@@    @@@@@@     @@@@            
            @@@@@@@@@@@@@@@@@@                                                                                                
              @@@@@@@@@@@@@@                                                                                                  
                 @@@@@@@@                                                                                                     
                                                                                                                                                                                                                                             
{Fore.WHITE}
""")

#DEVELOPER MODE
#You should leave this boolean off, enable only when smth is not okay...
#A Great option when the SQL server is down!
developer_mode = False #Edit: you still have to run the server, and set up the tables.

class SQLControll_Init(threading.Thread):
    def run(self):
        if developer_mode is False:
            global init_success
            init_success = False
            mydb = mysql.connector.connect(
            host = "127.0.0.1",
            port = 8080,
            user = "root",
            password = SQLPASSWORD,
            database = "token_storage"
            )
            mycursor = mydb.cursor()

            if mydb.is_connected:
                init_success = True
                pass
            else:
                init_success = False
                time.sleep(2)
                self.run()
        else:
            pass

class clickSoundThread(threading.Thread):
    def run(self):
        playsound(soundFile)

class SourceControll_Init(threading.Thread):
    def run(self):
        global EMPTUM_CONSOLE_PREFIX
        global init_success
        init_success = False
        if os.path.isfile(r"unloaded_processes.hs"):
            init_success = True
            pass
        else:
            with open(r'unloaded_processes.hs', 'x') as f:
                init_success = False
                f.write("Minecraft.exe;default\nLively.exe;default\nDiscord.exe;default\nVivaldi.exe;default\n")
                time.sleep(1)
                init_success = True
        if os.path.isfile(r"login_log.hs"):
            init_success = True
            pass
        else:
            with open(r'login_log.hs', 'x') as f:
                init_success = False
                f.write(f"{EMPTUM_CONSOLE_PREFIX}Created login log file at {current_date} {current_time}!")
                time.sleep(1)
                init_success = True
        if os.path.isfile(r"activity_log.hs"):
            init_success = True
            pass
        else:
            with open(r'activity_log.hs', 'x') as f:
                init_success = False
                f.write(f"{EMPTUM_CONSOLE_PREFIX}Created activity log file at {current_date} {current_time}!")
                time.sleep(1)
                init_success = True
        if os.path.isfile(r"addresses.sv"):
            init_success = True
            pass
        else:
            with open(r'addresses.sv', 'x') as f:
                init_success = False
                f.write("")
                time.sleep(1)
                init_success = True
        if os.path.isfile(r"machineid.sv"):
            init_success = True
            pass
        else:
            with open(r'machineid.sv', 'x') as f:
                init_success = False
                f.write("")
                time.sleep(1)
                init_success = True
        if os.path.isfile(r"scansettings.sv"):
            init_success = True
            pass
        else:
            with open(r'scansettings.sv', 'x') as f:
                init_success = False
                f.write("scan.wallpaper.wallon\nscan.installs.installson\nscan.startup.starton\nscan.runtime.runon")
                time.sleep(1)
                init_success = True

def init_bar(loading_steps, load_type):
    global init_success
    total_length = 40  # Total length of the loading bar
    fill_char = f'{Fore.WHITE}█'   # Character used to fill the loading bar
    empty_char = f'{Fore.MAGENTA}-'  # Character used for empty portion of the loading bar
        
    if load_type == 'source':
        source_control = SourceControll_Init()
        source_control.start()

    elif load_type == 'sql':
        sql_control = SQLControll_Init()
        sql_control.start()
    
    progress = 0
    while progress <= 100:
        filled_length = int(total_length * progress / 100)
        empty_length = total_length - filled_length
        
        bar = fill_char * filled_length + empty_char * empty_length
        percentage = f'{Fore.WHITE}{progress}%'
        
        sys.stdout.write('\r' + f'{Fore.MAGENTA}|{bar}{Fore.MAGENTA}| {percentage}')
        sys.stdout.flush()

        if init_success:
            progress += loading_steps
        else:
            pass

print(Fore.MAGENTA + f"[{Fore.WHITE}#{Fore.MAGENTA}]{Fore.WHITE}> Inintializing Sentry, please wait.", Fore.WHITE)
init_bar(2, 'source')

print(Fore.MAGENTA + f"\n[{Fore.WHITE}#{Fore.MAGENTA}]{Fore.WHITE}> Connecting to SQL server...", Fore.WHITE)
init_bar(100, 'sql')

print(Fore.MAGENTA + f"\n[{Fore.WHITE}#{Fore.MAGENTA}]{Fore.WHITE}> {Fore.GREEN}OK{Fore.WHITE}", Fore.WHITE)

print(EMPTUM_CONSOLE_PREFIX + f"Logged in Runtime as: {USER_NAME}" + " at " + current_time + "!")  
print(EMPTUM_CONSOLE_PREFIX + str(CWD_PATH) + ' - Current Working Directory.')
print(EMPTUM_CONSOLE_PREFIX + 'SENTRY is running in console. Interface with CUSTOMTKINTER.')
print(f'{EMPTUM_CONSOLE_PREFIX}Start checking logs, and shared values!')

import mysql.connector

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

def toastNotification(toast_id, toast_title, toast_msg, toast_icon_path, doLabel, toast_label, toast_launch):
    current_path = os.path.dirname(os.path.realpath(__file__))
    toast = Notification(app_id=toast_id, title=toast_title, msg=toast_msg, icon=str(CWD_PATH) + toast_icon_path)
    toast.set_audio(audio.Default, loop=False)
    toast.show()

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

def defineID():
    mydb = mysql.connector.connect(
            host = "127.0.0.1",
            port = 8080,
            user = "root",
            password = SQLPASSWORD,
            database = "token_storage"
        )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT machine_id FROM id_table")
    myresult = mycursor.fetchall()

    for x in myresult:
        idString = ''
        idString = str(x[0])
        print(f'{EMPTUM_CONSOLE_PREFIX}Machine ID found in SQL database: {idString}!')
        idList.append(idString)

    with open(r'machineid.sv', 'r+', encoding='utf-8') as f:
        if ' ' in f.read():
            print(f'{EMPTUM_CONSOLE_PREFIX}Machine ID: [{MACHINE_ID}]')
        else:
            print(f'{EMPTUM_CONSOLE_PREFIX}No Machine ID found, writing a new one!')
            
            f.write(str(len(idList) + 1) + ' ')
            print(f'{EMPTUM_CONSOLE_PREFIX}Machine ID Done!')
            sqlid = str(len(idList) + 1) + ' '
            sql = "INSERT INTO id_table (machine_id, machine) VALUES (%s, %s)"
            val = (sqlid, 'Windows Machine')
        
            mycursor.execute(sql, val)
            mydb.commit()

            print(f'{EMPTUM_CONSOLE_PREFIX}Machine ID wrote into the SQL database at {mydb._host}!')

def readID():
    global MACHINE_ID
    with open(r'machineid.sv', 'r') as idSharedValue:
        MACHINE_ID = idSharedValue.read().rstrip()

class BootScreen(threading.Thread):
    def run(self):
        # Run the other Python code
        subprocess.call(['python', 'boot.py'])

class ActivityThread(threading.Thread):
    def run(self):
        # Run the other Python code
        subprocess.call(['python', 'report.py'])

class WebThread(threading.Thread):
    def run(self):
        # Run the other Python code
        subprocess.call(['python', 'web.py'])

class InstallationsThread(threading.Thread):
    def run(self):
        # Run the other Python code
        subprocess.call(['python', 'installations.py'])

class AppsThread(threading.Thread):
    def run(self):
        # Run the other Python code
        subprocess.call(['python', 'apps.py'])


class AutoScan(threading.Thread):
    def run(self):
        subprocess.call(['python', 'scan.py'])
autoScan = AutoScan()
autoScan.start()


bootScreen = BootScreen()
bootScreen.start()

readID()
defineID()
time.sleep(5)
toastNotification('SENTRY - Better School Cyber Security', 'Welcome back!', 'SENTRY is ready to go!', r"\images\system_default_notification.ico", 'False', '', '')

class App(customtkinter.CTk):
    width = 500
    height = 486

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #FRAME SETUP
        #Setuping the borders, also sizeing the frame of the whole application.
        #Loading the background, and displaying the Sinope's name.
        self.title("SENTRY - Better School Cyber Security")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        if developer_mode: bg_path = "/images/runtime_background_dev.png"
        else: bg_path = "/images/runtime_background.png"

        self.bg_image = customtkinter.CTkImage(Image.open(current_path + bg_path),
                                            size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)
        self.iconpath = ImageTk.PhotoImage(file=os.path.join("images","runtime_icon.png"))
        self.wm_iconbitmap()
        self.iconphoto(False, self.iconpath)

        #LOGIN VARIABLES!
        self.usersList = []
        self.hashList = []

        #INJECTS
        self.INSTALLATIONS_INJECTS = []
        self.APPLICATION_INJECTS = []

        #MODIFY SETTINGS VARIABLES!
        self.wallpapertoogle = True
        self.installationstoogle = True
        self.startuptoogle = True
        self.runtimetoogle = True

        #LOGIN UI FRAME
        #The given data from the input fields are processed safely.
        self.login_frame = customtkinter.CTkFrame(self, bg_color= "#202020", corner_radius=(30))
        self.login_frame.grid(row=0)
        login_image = ImageTk.PhotoImage(Image.open(current_path + r"/images/sentry_logo.png"))
        self.fake_button_image = customtkinter.CTkButton(self.login_frame, text="", image = login_image, width=20, height=20, fg_color="#000000", hover_color="#000000", corner_radius=(30))
        self.fake_button_image .grid(row=1, column=0, padx=15, pady=(30, 10))
        self.banner = customtkinter.CTkLabel(self.login_frame, text='Welcome to SENTRY!\nA way for a Better School Cyber Security!',
                                                font=customtkinter.CTkFont(size=13))
        self.banner.grid(row=2, column=0, padx=15, pady=(10, 0))
        self.information_text = customtkinter.CTkLabel(self.login_frame, text='Please login with your name and password!',
                                                font=customtkinter.CTkFont(size=10))
        self.information_text.grid(row=3, column=0, padx=15, pady=(0, 0))
        border_image_login = ImageTk.PhotoImage(Image.open(current_path + r"/images/border.png"))
        self.fake_button_image = customtkinter.CTkButton(self.login_frame, text="", image = border_image_login, width=20, height=20, fg_color="#302c2c", hover_color="#302c2c")
        self.fake_button_image .grid(row=4, column=0, padx=15, pady=(0, 0))
        self.username_entry = customtkinter.CTkEntry(self.login_frame, width=200, placeholder_text="Name:")
        self.username_entry.grid(row=5, column=0, padx=30, pady=(0, 15))
        self.password_entry = customtkinter.CTkEntry(self.login_frame, width=200, show=".", placeholder_text="Password:")
        self.password_entry.grid(row=6, column=0, padx=30, pady=(0, 15))
        self.login_button = customtkinter.CTkButton(self.login_frame, fg_color="#984cfc", hover_color="#882cfc", text="Login", command=self.login_event, width=100)
        self.login_button.grid(row=7, column=0, padx=30, pady=(10, 15))
        self.banner = customtkinter.CTkLabel(self.login_frame, text="By using SENTRY you accept the EULA.\nBetter School Cyber Securty | SENTRY 2023-2024",
                                                 font=customtkinter.CTkFont(size=10))
        self.banner.grid(row=8, column=0, padx=15, pady=(0, 5))
        nikkeisadev_banner = ImageTk.PhotoImage(Image.open(current_path + r"/images/nikkeisadev_logo.png"))
        self.fake_button_image = customtkinter.CTkButton(self.login_frame, text="", image = nikkeisadev_banner, width=10, height=10, fg_color="#803fdf", hover_color="#803fdf", corner_radius=(30))
        self.fake_button_image .grid(row=9, column=0, padx=15, pady=(0, 20))
        

        #LOGGIN PASSED UI FRAME
        #If the token, and the username were correct, this page should be displayed.
        self.loggedin_frame = customtkinter.CTkFrame(self, corner_radius=0)
        completedlogin_image = ImageTk.PhotoImage(Image.open(current_path + r"/images/completed_login.png"))
        self.fake_button_image = customtkinter.CTkButton(self.loggedin_frame, text="", image = completedlogin_image, width=20, height=20, fg_color="#302c2c", hover_color="#302c2c")
        self.fake_button_image .grid(row=0, column=0, padx=15, pady=(50, 2))
        self.loggedin_welcome = customtkinter.CTkLabel(self.loggedin_frame, text="Success!",
                                                 font=customtkinter.CTkFont(size=40, weight="bold"))
        self.loggedin_welcome.grid(row=1, column=0, padx=15, pady=(0, 0))
        self.loggedin_welcometwo = customtkinter.CTkLabel(self.loggedin_frame, text="You successfuly logged in to SENTRY!\n",
                                                 font=customtkinter.CTkFont(size=10))
        self.loggedin_welcometwo.grid(row=2, column=0, padx=15, pady=(0, 0))
        self.loggedin_label = customtkinter.CTkLabel(self.loggedin_frame, text="\nClick on the Next button to continue to \nthe control panel. Login saved \n" + str(current_date) + " " + str(current_time),
                                                 font=customtkinter.CTkFont(size=12))
        self.loggedin_label.grid(row=3, column=0, padx=15, pady=(120, 0))
        self.newtoken_button = customtkinter.CTkButton(self.loggedin_frame, text="Request New Token", command=self.sendTokenRequest, width=200, fg_color="#984cfc", hover_color="#882cfc",)
        self.newtoken_button .grid(row=4, column=0, padx=15, pady=(16, 0))
        self.next_button = customtkinter.CTkButton(self.loggedin_frame, fg_color="#984cfc", hover_color="#882cfc", text="Next", command=self.next_event, width=200)
        self.next_button .grid(row=5, column=0, padx=15, pady=(6, 20))


        #LOGIN FAILED UI FRAME
        #This page only displays when you failed the login process.
        # - SQL DataBase required with the give informations, or use the SinopRegister.
        self.failed_frame = customtkinter.CTkFrame(self, corner_radius=0)
        failedlogin_image = ImageTk.PhotoImage(Image.open(current_path + r"/images/failed.png"))
        self.fake_button_image = customtkinter.CTkButton(self.failed_frame, text="", image = failedlogin_image, width=20, height=20, fg_color="#302c2c", hover_color="#302c2c")
        self.fake_button_image .grid(row=0, column=0, padx=15, pady=(6, 10))
        self.failed_message = customtkinter.CTkLabel(self.failed_frame, text="Login failed!",
                                                 font=customtkinter.CTkFont(size=30, weight="bold"))
        self.failed_message.grid(row=1, column=0, padx=15, pady=(0, 0))
        self.failed_messagetwo = customtkinter.CTkLabel(self.failed_frame, text="The password with the name\n can't be found!",
                                                 font=customtkinter.CTkFont(size=10))
        self.failed_messagetwo.grid(row=1, column=0, padx=15, pady=(60, 0))
        self.failed_label = customtkinter.CTkLabel(self.failed_frame, text="Can't log in? Contact the administrator \nfor a new login token.",
                                                 font=customtkinter.CTkFont(size=12))
        self.failed_label.grid(row=2, column=0, padx=15, pady=(120, 0))
        self.newtoken_button = customtkinter.CTkButton(self.failed_frame, text="Request New Token", command=self.backtologin_event, width=200, fg_color="#984cfc", hover_color="#882cfc",)
        self.newtoken_button .grid(row=3, column=0, padx=15, pady=(16, 0))
        self.back_button = customtkinter.CTkButton(self.failed_frame, text="Back", command=self.backtologin_event, width=200, fg_color="#984cfc", hover_color="#882cfc",)
        self.back_button .grid(row=4, column=0, padx=15, pady=(6, 20))
        
        
        #MAIN UI FRAME
        #Mainframe, the main back point of all functional frame.
        self.main_frame = customtkinter.CTkFrame(self, corner_radius=0)
        login_image = ImageTk.PhotoImage(Image.open(current_path + r"/images/sentry_logo.png"))
        self.fake_button_image = customtkinter.CTkButton(self.main_frame, text="", image = login_image, width=20, height=20, fg_color="#000000", hover_color="#000000", corner_radius=(30))
        self.fake_button_image .grid(row=1, column=0, padx=15, pady=(40, 4))
        self.usernamebanner = customtkinter.CTkLabel(self.main_frame, text="",
                                            font=customtkinter.CTkFont(size=10))
        self.usernamebanner.grid(row=2, column=0, padx=15, pady=(0, 6))
        border_image_login = ImageTk.PhotoImage(Image.open(current_path + r"/images/border.png"))
        self.fake_button_image = customtkinter.CTkButton(self.main_frame, text="", image = border_image_login, width=20, height=20, fg_color="#302c2c", hover_color="#302c2c")
        self.fake_button_image .grid(row=3, column=0, padx=15, pady=(0, 0))
        self.back_button  = customtkinter.CTkButton(self.main_frame, fg_color="#984cfc", hover_color="#882cfc", text="Scanning", command=self.open_expertscan, width=200)
        self.back_button .grid(row=4, column=0, padx=30, pady=(4, 4))
        self.back_button  = customtkinter.CTkButton(self.main_frame, fg_color="#984cfc", hover_color="#882cfc", text="Settings permission", command=self.open_winsettings, width=200)
        self.back_button .grid(row=5, column=0, padx=30, pady=(4, 4))
        self.back_button  = customtkinter.CTkButton(self.main_frame, fg_color="#984cfc", hover_color="#882cfc", text="Processes", command=self.open_add_app, width=200)
        self.back_button .grid(row=6, column=0, padx=30, pady=(4, 4))
        self.back_button  = customtkinter.CTkButton(self.main_frame, fg_color="#984cfc", hover_color="#882cfc", text="Installations", command=self.open_installations, width=200)
        self.back_button .grid(row=7, column=0, padx=30, pady=(4, 4))
        self.back_button  = customtkinter.CTkButton(self.main_frame, fg_color="#984cfc", hover_color="#882cfc", text="Web Control", command=self.open_webcontrollpanel, width=200)
        self.back_button .grid(row=8, column=0, padx=30, pady=(4, 4))
        self.back_button  = customtkinter.CTkButton(self.main_frame, fg_color="#984cfc", hover_color="#882cfc", text="Check Activity", command=self.launch_activity_reports, width=200)
        self.back_button .grid(row=9, column=0, padx=30, pady=(4, 4))
        self.back_button = customtkinter.CTkButton(self.main_frame, text="Logout", command=self.logout_event, width=200, fg_color="#eb3434", hover_color="#e01d1d")
        self.back_button .grid(row=10, column=0, padx=15, pady=(16, 0))
        self.banner = customtkinter.CTkLabel(self.main_frame, text="By using SENTRY you accept the EULA.\nBetter School Cyber Securty | SENTRY 2023-2024",
                                                 font=customtkinter.CTkFont(size=10))
        self.banner.grid(row=11, column=0, padx=15, pady=(5, 0))

        #FUNCTIONAL FRAMES JOINTED TO MAIN
        #These are the functional frames such as like runtime,wallpaper,web, and installation scannig.

        #SCANNING UI FRAME
        #The frame where you can start expertscan (as a function).
        self.scanning_frame = customtkinter.CTkFrame(self, corner_radius=0)
        login_image = ImageTk.PhotoImage(Image.open(current_path + r"/images/sentry_logo.png"))
        self.fake_button_image = customtkinter.CTkButton(self.scanning_frame, text="", image = login_image, width=20, height=20, fg_color="#000000", hover_color="#000000", corner_radius=(30))
        self.fake_button_image .grid(row=0, column=0, padx=15, pady=(40, 4))
        self.scanbanner = customtkinter.CTkLabel(self.scanning_frame, text="Scanning system.",
                                            font=customtkinter.CTkFont(size=20))
        self.scanbanner.grid(row=1, column=0, padx=15, pady=(20, 0))
        loadingbar = ImageTk.PhotoImage(Image.open(current_path + r"/images/border.png"))
        self.loadingbarimage = customtkinter.CTkButton(self.scanning_frame, text="", image = loadingbar, width=10, height=10, fg_color="#302c2c", hover_color="#302c2c")
        self.loadingbarimage.grid(row=2, column=0, padx=15, pady=(2, 0))
        self.scanbutton = customtkinter.CTkButton(self.scanning_frame, text="Start scan", command=self.EXPERTSCAN, width=200, fg_color="#eb3434", hover_color="#e01d1d")
        self.scanbutton .grid(row=4, column=0, padx=15, pady=(30, 0))
        self.back_button = customtkinter.CTkButton(self.scanning_frame, text="Go back", command=self.back_mainframe_from_scanstart, width=200, fg_color="#eb3434", hover_color="#e01d1d")
        self.back_button .grid(row=5, column=0, padx=15, pady=(5, 10))
        self.scantext = customtkinter.CTkLabel(self.scanning_frame, text="",
                                            font=customtkinter.CTkFont(size=10))
        self.scantext.grid(row=6, column=0, padx=15, pady=(0, 0))
        self.scanabout = customtkinter.CTkLabel(self.scanning_frame, text="The scan finishes in a few seconds.",
                                            font=customtkinter.CTkFont(size=10))
        self.scanabout.grid(row=7, column=0, padx=15, pady=(2, 7))
        self.banner = customtkinter.CTkLabel(self.scanning_frame, text="By using SENTRY you accept the EULA.\nBetter School Cyber Securty | SENTRY 2023-2024",
                                                 font=customtkinter.CTkFont(size=10))
        self.banner.grid(row=8, column=0, padx=15, pady=(0, 5))


        #MODIFY UI FRAME
        #Here, you can modify the settings of autoscan what should be checked such as runtime, and wallpaper.
        self.modify_frame = customtkinter.CTkFrame(self, corner_radius=0)
        completedlogin_image = ImageTk.PhotoImage(Image.open(current_path + r"/images/add_app.png"))
        self.fake_button_image = customtkinter.CTkButton(self.modify_frame, text="", image = completedlogin_image, width=20, height=20, fg_color="#302c2c", hover_color="#302c2c")
        self.fake_button_image .grid(row=0, column=0, padx=15, pady=(10, 2))
        self.loggedin_welcome = customtkinter.CTkLabel(self.modify_frame, text="Automatic scan",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.loggedin_welcome.grid(row=1, column=0, padx=15, pady=(0, 0))
        self.settings_banner = customtkinter.CTkLabel(self.modify_frame, text="Toogle the settings bellow of scanning.\nThe changes are being saved.",
                                                font=customtkinter.CTkFont(size=10))
        self.settings_banner.grid(row=2, column=0, padx=15, pady=(0, 2))
        border_image_login = ImageTk.PhotoImage(Image.open(current_path + r"/images/border.png"))
        self.fake_button_image = customtkinter.CTkButton(self.modify_frame, text="", image = border_image_login, width=20, height=20, fg_color="#302c2c", hover_color="#302c2c")
        self.fake_button_image .grid(row=3, column=0, padx=15, pady=(0, 6))
          
        
        self.wallpaper_button = customtkinter.CTkButton(self.modify_frame, text=" Wallpaper scan  ALLOWED", command=self.wallpaper_scan_toogle_off, width=20, fg_color="#984cfc", hover_color="#984cfc", 
                                                font=customtkinter.CTkFont(size=12))
        self.wallpaper_button .grid(row=4, column=0, padx=(0, 0), pady=(5, 10))
        self.installs_button = customtkinter.CTkButton(self.modify_frame, text="Installations scan ALLOWED", command=self.installations_scan_toogle_off, width=20, fg_color="#984cfc", hover_color="#984cfc", 
                                                font=customtkinter.CTkFont(size=12))
        self.installs_button .grid(row=5, column=0, padx=(0, 0), pady=(0, 10))
        self.startup_button = customtkinter.CTkButton(self.modify_frame, text="  Startup scan      ALLOWED", command=self.startup_scan_toogle_off, width=20, fg_color="#984cfc", hover_color="#984cfc", 
                                                font=customtkinter.CTkFont(size=12))
        self.startup_button .grid(row=6, column=0, padx=(0, 0), pady=(0, 10))
        self.runtime_button = customtkinter.CTkButton(self.modify_frame, text="  Runtime scan      ALLOWED", command=self.runtime_scan_toogle_off, width=20, fg_color="#984cfc", hover_color="#984cfc", 
                                                font=customtkinter.CTkFont(size=12))
        self.runtime_button .grid(row=7, column=0, padx=(0, 0), pady=(0, 10))
        
        

        self.resetconfig = customtkinter.CTkButton(self.modify_frame, text="RESET CONFIG FILE", command=self.resetscanconfig, width=20, fg_color="#eb3434", hover_color="#eb3434", 
                                                font=customtkinter.CTkFont(size=13))
        self.resetconfig .grid(row=9, column=0, padx=(0, 0), pady=(0, 10))
        

        self.back_button = customtkinter.CTkButton(self.modify_frame, text="Back", command=self.back_expertscan_from_modify, width=200, fg_color="#eb3434", hover_color="#e01d1d")
        self.back_button .grid(row=10, column=0, padx=15, pady=(5, 10))
        self.banner = customtkinter.CTkLabel(self.modify_frame, text="By using SENTRY you accept the EULA.\nBetter School Cyber Securty | SENTRY 2023-2024",
                                                 font=customtkinter.CTkFont(size=10))
        self.banner.grid(row=11, column=0, padx=15, pady=(0, 50))

        #RUNTIME UI FRAME
        self.add_app_frame = customtkinter.CTkFrame(self, corner_radius=0)
        addapplicationimage = ImageTk.PhotoImage(Image.open(current_path + r"/images/add_app.png"))
        self.fake_button_image = customtkinter.CTkButton(self.add_app_frame, text="", image = addapplicationimage, width=20, height=20, fg_color="#302c2c", hover_color="#302c2c")
        self.fake_button_image .grid(row=0, column=0, padx=15, pady=(17, 2))
        self.loggedin_welcome = customtkinter.CTkLabel(self.add_app_frame, text="Processes",
                                                 font=customtkinter.CTkFont(size=25, weight="bold"))
        self.loggedin_welcome.grid(row=1, column=0, padx=15, pady=(0, 0))
        self.loggedin_welcometwo = customtkinter.CTkLabel(self.add_app_frame, text="Want to add a Blacklisted application?\nOnly .exe format accepted as input!",
                                                 font=customtkinter.CTkFont(size=10))
        borderimage = ImageTk.PhotoImage(Image.open(current_path + r"/images/border.png"))
        self.fake_button_image = customtkinter.CTkButton(self.add_app_frame, text="", image = borderimage, width=0, height=0, fg_color="#302c2c", hover_color="#302c2c")
        self.fake_button_image .grid(row=2, column=0, padx=15, pady=(10, 2))
        self.loggedin_welcometwo = customtkinter.CTkLabel(self.add_app_frame, text="Not sure which application is added?\nCheck them by clicking here!",
                                            font=customtkinter.CTkFont(size=12))
        self.loggedin_welcometwo.grid(row=4, column=0, padx=15, pady=(23, 5))
        self.check_apps = customtkinter.CTkButton(self.add_app_frame, text="Check Apps", command=self.launch_apps_ui, width=200, fg_color="#984cfc", hover_color="#882cfc")
        self.check_apps .grid(row=5, column=0, padx=15, pady=(0, 0))
        self.loggedin_label = customtkinter.CTkLabel(self.add_app_frame, text="Press the button to save the application!\nThe next automatized scan will read it!",
                                                 font=customtkinter.CTkFont(size=12))
        self.loggedin_label.grid(row=6, column=0, padx=15, pady=(36, 3))
        self.illegal_process = customtkinter.CTkEntry(self.add_app_frame, width=200, placeholder_text="Give a Blacklisted process: ")
        self.illegal_process.grid(row=7, column=0, padx=30, pady=(5, 3))
        self.addillegal_process = customtkinter.CTkButton(self.add_app_frame, text="Add Process", command=self.add_illegal_process, width=200, fg_color="#984cfc", hover_color="#882cfc")
        self.addillegal_process .grid(row=8, column=0, padx=15, pady=(0, 0))
        self.addillegal_process = customtkinter.CTkButton(self.add_app_frame, text="Remove Process", command=self.remove_illegal_process, width=200, fg_color="#984cfc", hover_color="#882cfc")
        self.addillegal_process .grid(row=9, column=0, padx=15, pady=(3, 0))
        self.back_button = customtkinter.CTkButton(self.add_app_frame, text="Back", command=self.back_mainframe_from_apps, width=200, fg_color="#eb3434", hover_color="#e01d1d")
        self.back_button .grid(row=10, column=0, padx=15, pady=(15, 10))
        self.banner = customtkinter.CTkLabel(self.add_app_frame, text="By using SENTRY you accept the EULA.\nBetter School Cyber Securty | SENTRY 2023-2024",
                                                 font=customtkinter.CTkFont(size=10))
        self.banner.grid(row=11, column=0, padx=15, pady=(0, 2))
        
        
        #EXPERTSCAN UI FRAME
        self.expertscan_frame = customtkinter.CTkFrame(self, corner_radius=0)
        expertscanimage = ImageTk.PhotoImage(Image.open(current_path + r"/images/scan_system_expert.png"))
        self.fake_button_image = customtkinter.CTkButton(self.expertscan_frame, text="", image = expertscanimage, width=0, height=0, fg_color="#302c2c", hover_color="#302c2c")
        self.fake_button_image .grid(row=0, column=0, padx=15, pady=(40, 2))
        self.loggedin_welcome = customtkinter.CTkLabel(self.expertscan_frame, text="Scanning",
                                                 font=customtkinter.CTkFont(size=30, weight="bold"))
        self.loggedin_welcome.grid(row=1, column=0, padx=15, pady=(0, 0))
        self.loggedin_welcometwo = customtkinter.CTkLabel(self.expertscan_frame, text="Here, you can modify and run scanning\nprocesses in your system.",
                                                 font=customtkinter.CTkFont(size=10))
        self.loggedin_welcometwo.grid(row=2, column=0, padx=15, pady=(0, 0))
        purpleborderimage = ImageTk.PhotoImage(Image.open(current_path + r"/images/border.png"))
        self.border_button_image = customtkinter.CTkButton(self.expertscan_frame, text="", image = purpleborderimage, width=0, height=0, fg_color="#302c2c", hover_color="#302c2c")
        self.border_button_image .grid(row=3, column=0, padx=15, pady=(3, 3))
        self.autoscan_label = customtkinter.CTkLabel(self.expertscan_frame, text="Want to change the automatized scan?\nYou can select the actions here!",
                                                 font=customtkinter.CTkFont(size=12))
        self.autoscan_label.grid(row=4, column=0, padx=15, pady=(30, 3))
        self.addillegal_process = customtkinter.CTkButton(self.expertscan_frame, text="Automatic scan", command=self.open_modify, width=200, fg_color="#984cfc", hover_color="#882cfc")
        self.addillegal_process .grid(row=5, column=0, padx=15, pady=(10, 0))
        self.loggedin_label = customtkinter.CTkLabel(self.expertscan_frame, text="Click on the button to start scanning.\nThe scan is about a few secounds.",
                                                 font=customtkinter.CTkFont(size=12))
        self.loggedin_label.grid(row=6, column=0, padx=15, pady=(20, 3))
        self.addillegal_process = customtkinter.CTkButton(self.expertscan_frame, text="Scan", command=self.startscanonce, width=200, fg_color="#984cfc", hover_color="#882cfc")
        self.addillegal_process .grid(row=7, column=0, padx=15, pady=(10, 0))
        self.back_button = customtkinter.CTkButton(self.expertscan_frame, text="Back", command=self.back_mainframe_from_expertscan, width=200, fg_color="#eb3434", hover_color="#e01d1d")
        self.back_button .grid(row=8, column=0, padx=15, pady=(3, 10))
        self.banner = customtkinter.CTkLabel(self.expertscan_frame, text="By using SENTRY you accept the EULA.\nBetter School Cyber Securty | SENTRY 2023-2024",
                                                 font=customtkinter.CTkFont(size=10))
        self.banner.grid(row=9, column=0, padx=15, pady=(0, 5))
        
        
        #SETTINGS UI FRAME
        self.windowssettings_frame = customtkinter.CTkFrame(self, corner_radius=0)
        expertscanimage = ImageTk.PhotoImage(Image.open(current_path + r"/images/win_settings.png"))
        self.fake_button_image = customtkinter.CTkButton(self.windowssettings_frame, text="", image = expertscanimage, width=0, height=0, fg_color="#302c2c", hover_color="#302c2c")
        self.fake_button_image .grid(row=0, column=0, padx=15, pady=(40, 2))
        self.loggedin_welcome = customtkinter.CTkLabel(self.windowssettings_frame, text="Settings permission",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.loggedin_welcome.grid(row=1, column=0, padx=15, pady=(0, 0))
        self.loggedin_welcometwo = customtkinter.CTkLabel(self.windowssettings_frame, text="Want to deny the settings in the system?\nYou can deny and allow it bellow.",
                                                 font=customtkinter.CTkFont(size=10))
        self.loggedin_welcometwo.grid(row=2, column=0, padx=15, pady=(0, 0))
        self.loggedin_label = customtkinter.CTkLabel(self.windowssettings_frame, text="Only works with administrator privileges.",
                                                 font=customtkinter.CTkFont(size=12))
        self.loggedin_label.grid(row=4, column=0, padx=15, pady=(120, 3))
        self.turnon_settings_button  = customtkinter.CTkButton(self.windowssettings_frame, fg_color="#984cfc", hover_color="#882cfc", text="Block Settings", command=self.on_settingsperm, width=200)
        self.turnon_settings_button .grid(row=5, column=0, padx=30, pady=(4, 4))
        self.turnoff_settings_button  = customtkinter.CTkButton(self.windowssettings_frame, fg_color="#984cfc", hover_color="#882cfc", text="Allow Settings ", command=self.off_settingsperm, width=200)
        self.turnoff_settings_button .grid(row=6, column=0, padx=30, pady=(4, 4))

        self.back_button = customtkinter.CTkButton(self.windowssettings_frame, text="Back", command=self.back_mainframe_from_win_settings, width=200, fg_color="#eb3434", hover_color="#e01d1d")
        self.back_button .grid(row=7, column=0, padx=15, pady=(3, 10))
        self.banner = customtkinter.CTkLabel(self.windowssettings_frame, text="By using SENTRY you accept the EULA.\nBetter School Cyber Securty | SENTRY 2023-2024",
                                                 font=customtkinter.CTkFont(size=10))
        self.banner.grid(row=8, column=0, padx=15, pady=(0, 5))
        
        
        #WEBSITES UI FRAME
        self.web_block_frame = customtkinter.CTkFrame(self, corner_radius=0)
        addapplicationimage = ImageTk.PhotoImage(Image.open(current_path + r"/images/webcontroll.png"))
        self.fake_button_image = customtkinter.CTkButton(self.web_block_frame, text="", image = addapplicationimage, width=20, height=20, fg_color="#302c2c", hover_color="#302c2c")
        self.fake_button_image .grid(row=0, column=0, padx=15, pady=(17, 2))
        self.loggedin_welcome = customtkinter.CTkLabel(self.web_block_frame, text="Web Control",
                                                 font=customtkinter.CTkFont(size=24, weight="bold"))
        self.loggedin_welcome.grid(row=1, column=0, padx=15, pady=(0, 0))
        borderimage = ImageTk.PhotoImage(Image.open(current_path + r"/images/border.png"))
        self.fake_button_image = customtkinter.CTkButton(self.web_block_frame, text="", image = borderimage, width=0, height=0, fg_color="#302c2c", hover_color="#302c2c")
        self.fake_button_image .grid(row=3, column=0, padx=15, pady=(10, 2))
        self.loggedin_welcometwo = customtkinter.CTkLabel(self.web_block_frame, text="Not sure which webpage is added?\nCheck them by clicking here!",
                                            font=customtkinter.CTkFont(size=12))
        self.loggedin_welcometwo.grid(row=4, column=0, padx=15, pady=(15, 5))
        self.check_sites = customtkinter.CTkButton(self.web_block_frame, text="Check Pages", command=self.launch_web_ui, width=200, fg_color="#984cfc", hover_color="#882cfc")
        self.check_sites .grid(row=5, column=0, padx=15, pady=(0, 0))
        self.loggedin_label = customtkinter.CTkLabel(self.web_block_frame, text="Write the name of the webpage\nthen press add button!",
                                                 font=customtkinter.CTkFont(size=12))
        self.loggedin_label.grid(row=6, column=0, padx=15, pady=(5, 3))
        self.forbidden_webpage = customtkinter.CTkEntry(self.web_block_frame, width=200, placeholder_text="Webpage name: ")
        self.forbidden_webpage.grid(row=7, column=0, padx=30, pady=(5, 3))
        self.addforbidden_webpage = customtkinter.CTkButton(self.web_block_frame, text="Add Webpage", command=self.add_forbidden_website, width=200, fg_color="#984cfc", hover_color="#882cfc")
        self.addforbidden_webpage .grid(row=8, column=0, padx=15, pady=(0, 0))
        self.runinject_button = customtkinter.CTkButton(self.web_block_frame, text="Remove Webpage", command=self.remove_blocked_site, width=200, fg_color="#984cfc", hover_color="#882cfc")
        self.runinject_button .grid(row=9, column=0, padx=15, pady=(3, 0))
        self.runinject_button = customtkinter.CTkButton(self.web_block_frame, text="Block Pages", command=self.block_webaddress, width=200, fg_color="#984cfc", hover_color="#882cfc")
        self.runinject_button .grid(row=10, column=0, padx=15, pady=(3, 0))
        self.clearcache_button = customtkinter.CTkButton(self.web_block_frame, text="Clear Cache", command=self.clearwebcache, width=200, fg_color="#984cfc", hover_color="#882cfc")
        self.clearcache_button .grid(row=11, column=0, padx=15, pady=(3, 10))
        self.back_button = customtkinter.CTkButton(self.web_block_frame, text="Back", command=self.back_mainframe_from_web_controll, width=200, fg_color="#eb3434", hover_color="#e01d1d")
        self.back_button .grid(row=12, column=0, padx=15, pady=(0, 10))
        
        
        #INSTALLATIONS UI FRAME
        self.installations_frame = customtkinter.CTkFrame(self, corner_radius=0)
        addapplicationimage = ImageTk.PhotoImage(Image.open(current_path + r"/images/installations.png"))
        self.fake_button_image = customtkinter.CTkButton(self.installations_frame, text="", image = addapplicationimage, width=20, height=20, fg_color="#302c2c", hover_color="#302c2c")
        self.fake_button_image .grid(row=0, column=0, padx=15, pady=(17, 2))
        self.loggedin_welcome = customtkinter.CTkLabel(self.installations_frame, text="Installations",
                                                 font=customtkinter.CTkFont(size=24, weight="bold"))
        self.loggedin_welcome.grid(row=1, column=0, padx=15, pady=(0, 0))
        borderimage = ImageTk.PhotoImage(Image.open(current_path + r"/images/border.png"))
        self.fake_button_image = customtkinter.CTkButton(self.installations_frame, text="", image = borderimage, width=0, height=0, fg_color="#302c2c", hover_color="#302c2c")
        self.fake_button_image .grid(row=3, column=0, padx=15, pady=(10, 2))
        self.loggedin_welcometwo = customtkinter.CTkLabel(self.installations_frame, text="Wanna check which installation is blocked?",
                                            font=customtkinter.CTkFont(size=12))
        self.loggedin_welcometwo.grid(row=4, column=0, padx=15, pady=(15, 5))
        self.check_sites = customtkinter.CTkButton(self.installations_frame, text="Check Installations", command=self.launch_installations_ui, width=200, fg_color="#984cfc", hover_color="#882cfc")
        self.check_sites .grid(row=5, column=0, padx=15, pady=(0, 0))
        self.loggedin_label = customtkinter.CTkLabel(self.installations_frame, text="Write the name of the installation\nthen press add button!",
                                                 font=customtkinter.CTkFont(size=12))
        self.loggedin_label.grid(row=6, column=0, padx=15, pady=(10, 3))
        self.illegal_installation = customtkinter.CTkEntry(self.installations_frame, width=200, placeholder_text="Installation name: ")
        self.illegal_installation.grid(row=7, column=0, padx=30, pady=(5, 3))
        self.addforbidden_webpage = customtkinter.CTkButton(self.installations_frame, text="Add Installation", command=self.add_illegal_installations, width=200, fg_color="#984cfc", hover_color="#882cfc")
        self.addforbidden_webpage .grid(row=8, column=0, padx=15, pady=(0, 0))
        self.runinject_button = customtkinter.CTkButton(self.installations_frame, text="Remove Installation", command=self.remove_blocked_installation, width=200, fg_color="#984cfc", hover_color="#882cfc")
        self.runinject_button .grid(row=9, column=0, padx=15, pady=(3, 0))
        self.back_button = customtkinter.CTkButton(self.installations_frame, text="Back", command=self.back_mainframe_from_installations, width=200, fg_color="#eb3434", hover_color="#e01d1d")
        self.back_button .grid(row=12, column=0, padx=15, pady=(10, 30))
        self.banner = customtkinter.CTkLabel(self.installations_frame, text="By using SENTRY you accept the EULA.\nBetter School Cyber Securty | SENTRY 2023-2024",
                                                 font=customtkinter.CTkFont(size=10))
        self.banner.grid(row=13, column=0, padx=15, pady=(0, 5))
        
    def readingTable(self):
        self.usersList = []
        self.hashList = []
        
        mydb = mysql.connector.connect(
            host = "127.0.0.1",
            port = 8080,
            user = "root",
            password = SQLPASSWORD,
            database = "token_storage"
        )
        mycursor = mydb.cursor()

        mycursor.execute("SELECT user_name FROM user_token")
        myresult = mycursor.fetchall()

        for x in myresult:
            nameString = ''
            nameString = str(x[0])
            print(f'{EMPTUM_CONSOLE_PREFIX}Registered user found: {nameString}!')
            self.usersList.append(nameString)
        
        mycursor.execute("SELECT user_token FROM user_token")
        myresult = mycursor.fetchall()

        for x in myresult:
            loginTokenHash = ''
            loginTokenHash = str(x[0])
            self.hashList.append(loginTokenHash)


    def login_event(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.PASSWORD_INPUT = self.password_entry.get()
        self.USERNAME_INPUT = self.username_entry.get()
        if developer_mode != True:
            self.usersList = []
            self.hashList = []
            self.readingTable()
            self.passwhash = hashlib.sha256(bytes(self.PASSWORD_INPUT, encoding="utf-8")).hexdigest()
        
            
            if self.usersList.__contains__(self.USERNAME_INPUT) and self.hashList.__contains__(self.passwhash):
                print(f'{EMPTUM_CONSOLE_PREFIX}Token, and username found in database! Now checking the login credentials...')
                
                userIndex = self.usersList.index(self.USERNAME_INPUT)
                hashIndex = self.hashList.index(self.passwhash)
            
                if userIndex == hashIndex:
                    print(f'{EMPTUM_CONSOLE_PREFIX}Login Successful as {self.USERNAME_INPUT}!')
                    self.usernamebanner = customtkinter.CTkLabel(self.main_frame, text=f"Welcome {self.USERNAME_INPUT}!\nPlease select an option bellow.",
                                            font=customtkinter.CTkFont(size=12))
                    self.usernamebanner.grid(row=2, column=0, padx=15, pady=(6, 6))
                    with open('login_log.hs', 'a', encoding='utf-8') as hs:
                        hs.write(f'Logged in successfuly at {current_date}, {current_time}!\nLogind save at loing_log.hs!\n==================SAVED==================\n')
                        hs.close()
                        self.login_frame.grid_forget()  # remove login frame
                        self.loggedin_frame.grid(row=0, column=0, sticky="nsew", padx=130)  # show main frame    
                else:
                    print(f'{EMPTUM_CONSOLE_PREFIX}The login credentials were wrong! ')
                    self.login_frame.grid_forget()  # remove login frame
                    self.failed_frame.grid(row=0, column=0, sticky="nsew", padx=130)  # show main frame
            else:
                print(f'{EMPTUM_CONSOLE_PREFIX}The login credentials were wrong! Not even found in the database...')
                self.login_frame.grid_forget()  # remove login frame
                self.failed_frame.grid(row=0, column=0, sticky="nsew", padx=130)  # show main frame
        
        elif self.PASSWORD_INPUT == self.USERNAME_INPUT:
                print(f'{EMPTUM_CONSOLE_PREFIX}The login credentials were wrong! ')
                self.login_frame.grid_forget()  # remove login frame
                self.loggedin_frame.grid(row=0, column=0, sticky="nsew", padx=100)  # show main frame    
                self.usernamebanner = customtkinter.CTkLabel(self.main_frame, text=f"Welcome {self.USERNAME_INPUT}!\nYou are in developer mode! The SQL communication is reduced.\n{current_path}",
                                        font=customtkinter.CTkFont(size=10))
                self.usernamebanner.grid(row=2, column=0, padx=15, pady=(6, 6))
                    
        elif self.PASSWORD_INPUT != self.USERNAME_INPUT:
                self.login_frame.grid_forget()  # remove login frame
                self.failed_frame.grid(row=0, column=0, sticky="nsew", padx=130)  # show main frame
            

    #LOGIN TOKEN CHECKING - EXPRIRE
    def isTokenLatest(self):
        if developer_mode != True:
            self.usersList = []
            self.hashList = []
            self.readingTable()
            
            print(f'{EMPTUM_CONSOLE_PREFIX}Checking the login token, is that the latest?')
            
            if self.usersList.__contains__(self.USERNAME_INPUT) and self.hashList.__contains__(self.passwhash):
                print(f'{EMPTUM_CONSOLE_PREFIX}Token, and username is valid, checking token.')
                
                userIndex = self.usersList.index(self.USERNAME_INPUT)
                hashIndex = self.hashList.index(self.passwhash)
            
                if userIndex == hashIndex:
                    print(f'{EMPTUM_CONSOLE_PREFIX}The token is still valid, Skipping...')
                else:
                    print(f'{EMPTUM_CONSOLE_PREFIX}[!] The token is invalid, closing session, logging out!')
                    toastNotification('SENTRY - Better School Cyber Security', 'Your token changed by an Administrator!', 'The session clossed, please contact the system administrator!', r"\images/system_alert.ico", 'False', '', '')
                    exit()
            else:
                print(f'{EMPTUM_CONSOLE_PREFIX}[!] The token is invalid, closing session, logging out!')
                toastNotification('SENTRY - Better School Cyber Security', 'Your token changed by an Administrator!', 'The session clossed, please contact the system administrator!', r"\images/system_alert.ico", 'False', '', '')
                exit()
        else:
            pass

    def sendTokenRequest(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        mydb = mysql.connector.connect(
            host = "127.0.0.1",
            port = 8080,
            user = "root",
            password = SQLPASSWORD,
            database = "token_storage"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO token_requests_table (request_table, username_table, hash_value) VALUES (%s, %s, %s)"
        val = ('Pending new token request from', self.USERNAME_INPUT, hashlib.sha256(bytes(self.PASSWORD_INPUT, encoding="utf-8")).hexdigest())
        
        mycursor.execute(sql, val)
        mydb.commit()

        print(f'{EMPTUM_CONSOLE_PREFIX}New token request sent from {self.USERNAME_INPUT}!')
        
    def modifyautoscan(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.isTokenLatest()
        print(f"{EMPTUM_CONSOLE_PREFIX}Opening Autoscan modifying frame!")
    
    def next_event(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.isTokenLatest()
        self.loggedin_frame.grid_forget()  # remove login frame
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=90)  # show main frame
    
    def startscanonce(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.isTokenLatest()
        self.EXPERTSCANLOAD()
    
    def open_expertscan(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.isTokenLatest()
        self.main_frame.grid_forget()  # remove login frame
        self.expertscan_frame.grid(row=0, column=0, sticky="nsew", padx=120)
    
    def open_webcontrollpanel(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.isTokenLatest()
        self.main_frame.grid_forget()  # remove login frame
        self.web_block_frame.grid(row=0, column=0, sticky="nsew", padx=120)
    
    def open_winsettings(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.isTokenLatest()
        self.main_frame.grid_forget()  # remove login frame
        self.windowssettings_frame.grid(row=0, column=0, sticky="nsew", padx=120)  
    
    def open_installations(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.isTokenLatest()
        self.main_frame.grid_forget()  # remove login frame
        self.installations_frame.grid(row=0, column=0, sticky="nsew", padx=120) 

    def back_mainframe_from_installations(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.isTokenLatest()
        self.installations_frame.grid_forget()  # remove login frame
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=90) 
    
    def back_mainframe_from_apps(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.isTokenLatest()
        self.add_app_frame.grid_forget()  # remove login frame
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=90)
    
    def back_mainframe_from_expertscan(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.isTokenLatest()
        self.expertscan_frame.grid_forget()  # remove login frame
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=90)
    
    def back_mainframe_from_win_settings(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.isTokenLatest()
        self.windowssettings_frame.grid_forget()  # remove login frame
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=90)
    
    def back_mainframe_from_web_controll(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.isTokenLatest()
        self.web_block_frame.grid_forget()  # remove login frame
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=90)
    
    def back_mainframe_from_scanstart(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.isTokenLatest()
        self.scanning_frame.grid_forget()  # remove login frame
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=90)

    def back_expertscan_from_modify(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.isTokenLatest()
        self.modify_frame.grid_forget()  # remove login frame
        self.expertscan_frame.grid(row=0, column=0, sticky="nsew", padx=120)
    
    def open_add_app(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.isTokenLatest()
        self.main_frame.grid_forget()  # remove login frame
        self.add_app_frame.grid(row=0, column=0, sticky="nsew", padx=120)
    
    def back_event(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.isTokenLatest()
        self.EXPERTSCAN()
    
    def launch_activity_reports(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        activity = ActivityThread()
        activity.start()
    def launch_apps_ui(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        apps = AppsThread()
        apps.start()
    def launch_web_ui(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        web = WebThread()
        web.start()
    def launch_installations_ui(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        installation = InstallationsThread()
        installation.start()

    def open_modify(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        with open(r'scansettings.sv', 'r') as fp:
            lines = fp.readlines()
            for row in lines:
                if row.find('walloff') != -1:
                    self.wallpaper_scan_toogle_off()
                if row.find('installsoff') != -1:
                    self.installations_scan_toogle_off()
                if row.find('startoff') != -1:
                    self.startup_scan_toogle_off()
                if row.find('runtimeoff') != -1:
                    self.runtime_scan_toogle_off()
        self.isTokenLatest()
        self.expertscan_frame.grid_forget()  # remove login frame
        self.modify_frame.grid(row=0, column=0, sticky="nsew", padx=120)

    def on_settingsperm(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.isTokenLatest()
        os.system(r"reg_settings_inject.bat")
        print(EMPTUM_CONSOLE_PREFIX + "Switching the permissions for the Windows Machine's settings.")
    
    def off_settingsperm(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.isTokenLatest()
        os.system(r"reg_settings_unlock.bat")
        print(EMPTUM_CONSOLE_PREFIX + "Switching the permissions for the Windows Machine's settings.")
    
    def backtologin_event(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.failed_frame.grid_forget()  # remove login frame
        self.login_frame.grid(row=0, column=0, sticky="nsew", padx=100, pady=20)  # show main frame
    
    def logout_event(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.isTokenLatest()
        self.main_frame.grid_forget()  # remove login frame
        self.login_frame.grid(row=0, column=0, sticky="nsew", padx=100, pady=20)  # show main frame
    
    def block_webaddress(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.isTokenLatest()
        print(f'{EMPTUM_CONSOLE_PREFIX}Blocking webpage!')
        os.system(r'host_settings_block.bat')
    
    #Scan modify definitions.
    def wallpaper_scan_toogle_off(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.wallpapertoogle = False
        self.wallpaper_button = customtkinter.CTkButton(self.modify_frame, text="   Wallpaper scan  DENIED  ", command=self.wallpaper_scan_toogle_on, width=20, fg_color="#eb3434", hover_color="#eb3434", 
                                            font=customtkinter.CTkFont(size=12))
        self.wallpaper_button .grid(row=4, column=0, padx=(0, 0), pady=(5, 10))
        self.mixscansettings()

    def wallpaper_scan_toogle_on(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.wallpapertoogle = True
        self.wallpaper_button = customtkinter.CTkButton(self.modify_frame, text=" Wallpaper scan  ALLOWED", command=self.wallpaper_scan_toogle_off, width=20, fg_color="#984cfc", hover_color="#984cfc", 
                                                font=customtkinter.CTkFont(size=12))
        self.wallpaper_button .grid(row=4, column=0, padx=(0, 0), pady=(5, 10))
        self.mixscansettings()

    def installations_scan_toogle_off(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.installationstoogle = False
        self.installations_button = customtkinter.CTkButton(self.modify_frame, text="  Installations scan  DENIED  ", command=self.installations_scan_toogle_on, width=20, fg_color="#eb3434", hover_color="#eb3434", 
                                            font=customtkinter.CTkFont(size=12))
        self.installations_button .grid(row=5, column=0, padx=(0, 0), pady=(0, 10))
        self.mixscansettings() 

    def resetscanconfig(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        
        with open(r'scansettings.sv', 'w') as f:
            f.write("scan.wallpaper.wallon\nscan.installs.installson\nscan.startup.starton\nscan.runtime.runon")
        
        self.wallpapertoogle = True
        self.wallpaper_button = customtkinter.CTkButton(self.modify_frame, text=" Wallpaper scan  ALLOWED", command=self.wallpaper_scan_toogle_off, width=20, fg_color="#984cfc", hover_color="#984cfc", 
                                                font=customtkinter.CTkFont(size=12))
        self.wallpaper_button .grid(row=4, column=0, padx=(0, 0), pady=(5, 10))
        self.installationstoogle = True
        self.installations_button = customtkinter.CTkButton(self.modify_frame, text="Installations scan  ALLOWED", command=self.installations_scan_toogle_off, width=20, fg_color="#984cfc", hover_color="#984cfc", 
                                                font=customtkinter.CTkFont(size=12))
        self.installations_button .grid(row=5, column=0, padx=(0, 0), pady=(0, 10))
        self.startuptoogle = True
        self.startup_button = customtkinter.CTkButton(self.modify_frame, text="   Startup scan      ALLOWED ", command=self.startup_scan_toogle_off, width=20, fg_color="#984cfc", hover_color="#984cfc", 
                                                font=customtkinter.CTkFont(size=12))
        self.startup_button .grid(row=6, column=0, padx=(0, 0), pady=(0, 10))
        self.runtimetoogle = True
        self.runtime_button = customtkinter.CTkButton(self.modify_frame, text=" Runtime scan      ALLOWED ", command=self.runtime_scan_toogle_off, width=20, fg_color="#984cfc", hover_color="#984cfc", 
                                                font=customtkinter.CTkFont(size=12))
        self.runtime_button .grid(row=7, column=0, padx=(0, 0), pady=(0, 10))
        

    def installations_scan_toogle_on(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.installationstoogle = True
        self.installations_button = customtkinter.CTkButton(self.modify_frame, text="Installations scan  ALLOWED", command=self.installations_scan_toogle_off, width=20, fg_color="#984cfc", hover_color="#984cfc", 
                                                font=customtkinter.CTkFont(size=12))
        self.installations_button .grid(row=5, column=0, padx=(0, 0), pady=(0, 10))
        self.mixscansettings()

    def startup_scan_toogle_off(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.startuptoogle = False
        self.startup_button = customtkinter.CTkButton(self.modify_frame, text="     Startup scan      DENIED   ", command=self.startup_scan_toogle_on, width=20, fg_color="#eb3434", hover_color="#eb3434", 
                                            font=customtkinter.CTkFont(size=12))
        self.startup_button .grid(row=6, column=0, padx=(0, 0), pady=(0, 10))
        self.mixscansettings()

    def startup_scan_toogle_on(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.startuptoogle = True
        self.startup_button = customtkinter.CTkButton(self.modify_frame, text="   Startup scan      ALLOWED ", command=self.startup_scan_toogle_off, width=20, fg_color="#984cfc", hover_color="#984cfc", 
                                                font=customtkinter.CTkFont(size=12))
        self.startup_button .grid(row=6, column=0, padx=(0, 0), pady=(0, 10))
        self.mixscansettings()

    def runtime_scan_toogle_off(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.runtimetoogle = False
        self.startup_button = customtkinter.CTkButton(self.modify_frame, text="   Runtime scan      DENIED   ", command=self.runtime_scan_toogle_on, width=20, fg_color="#eb3434", hover_color="#eb3434", 
                                            font=customtkinter.CTkFont(size=12))
        self.startup_button .grid(row=7, column=0, padx=(0, 0), pady=(0, 10))
        self.mixscansettings()

    def runtime_scan_toogle_on(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.runtimetoogle = True
        self.runtime_button = customtkinter.CTkButton(self.modify_frame, text=" Runtime scan      ALLOWED ", command=self.runtime_scan_toogle_off, width=20, fg_color="#984cfc", hover_color="#984cfc", 
                                                font=customtkinter.CTkFont(size=12))
        self.runtime_button .grid(row=7, column=0, padx=(0, 0), pady=(0, 10))
        self.mixscansettings()

    def add_illegal_process(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.isTokenLatest()
        defineApplicationKeysLoaded()

        notBreaked = True
        ILLEGAL_PROCESS_NAME = self.illegal_process.get()

        if '.exe' in ILLEGAL_PROCESS_NAME and ILLEGAL_PROCESS_NAME != '' and ILLEGAL_PROCESS_NAME != ' ':
            print(f'{EMPTUM_CONSOLE_PREFIX}The process name was valid! Added to the list. [APP: {ILLEGAL_PROCESS_NAME}] [TIME:{raw_datetime()}]')

            for index in APPLICATION_KEYS_LOADED:
               if index["app"].lower() == ILLEGAL_PROCESS_NAME.lower():
                    notBreaked = False
            
            if notBreaked:
                with open('unloaded_processes.hs', 'a', encoding='utf-8') as hs:
                    hs.write(f'{ILLEGAL_PROCESS_NAME};{raw_datetime()}\n')
                    hs.close()
                    toastNotification('SENTRY - Better School Cyber Security', 'New Blacklisted apps added!', f"You successfuly added a new Blacklisted application! ({ILLEGAL_PROCESS_NAME})", r"\images/system_scan_fine.ico", 'False', '', '')
            elif notBreaked == False:
                print(f'{EMPTUM_CONSOLE_PREFIX}The process name was invalid! Already defined in the database!')
        else:
            print(f'{EMPTUM_CONSOLE_PREFIX}The name of the process was incorrect! ')
    
    def add_illegal_installations(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.isTokenLatest()
        ILLEGAL_INSTALLATION_NAME = self.illegal_installation.get()
        if ILLEGAL_INSTALLATION_NAME == ' ' or ILLEGAL_INSTALLATION_NAME == '':
            pass
        else:
            with open('installations.hs', 'a', encoding='utf-8') as hs:
                hs.write(f'{ILLEGAL_INSTALLATION_NAME};{raw_datetime()}\n')
                hs.close()
            toastNotification('SENTRY - Better School Cyber Security', 'New Blacklisted installation added!', f"You successfuly added a new Blacklisted installation! ({ILLEGAL_INSTALLATION_NAME})", r"\images/system_scan_fine.ico", 'False', '', '')

    def remove_illegal_process(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        ILLEGAL_PROCESS_NAME = self.illegal_process.get()
        orig_lines = [line.strip() for line in open(r'unloaded_processes.hs')]
        new_lines = [l for l in orig_lines if not l.__contains__(ILLEGAL_PROCESS_NAME)]
        with open(r'unloaded_processes.hs', 'w') as fp:
            print(*new_lines, sep='\n', file=fp)
    
    def remove_blocked_installation(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        BLOCKED_INSTALLATION = self.illegal_installation.get()
        orig_lines = [line.strip() for line in open(r'installations.hs')]
        new_lines = [l for l in orig_lines if not l.__contains__(BLOCKED_INSTALLATION)]
        with open(r'installations.hs', 'w') as fp:
            print(*new_lines, sep='\n', file=fp)
    
    def remove_blocked_site(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        BLOCKED_SITE = self.forbidden_webpage.get()
        orig_lines = [line.strip() for line in open(r'addresses.sv')]
        new_lines = [l for l in orig_lines if not l.__contains__(BLOCKED_SITE)]
        with open(r'addresses.sv', 'w') as fp:
            print(*new_lines, sep='\n', file=fp)
        self.block_webaddress()
        
    def add_forbidden_website(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.isTokenLatest()
        FORRBIDEN_WEBPAGE = self.forbidden_webpage.get()
        if '.' in FORRBIDEN_WEBPAGE and FORRBIDEN_WEBPAGE != '' and FORRBIDEN_WEBPAGE != ' ':
            print(f'{EMPTUM_CONSOLE_PREFIX}The webaddress is correct! [WEB: {FORRBIDEN_WEBPAGE}] [TIME: {raw_datetime()}]')  
            with open('addresses.sv', 'a', encoding='utf-8') as hs:
                hs.write(f'127.0.0.1 {FORRBIDEN_WEBPAGE.lower()}\n127.0.0.1 www.{FORRBIDEN_WEBPAGE.lower()}\n')
                hs.close()
            toastNotification('SENTRY - Better School Cyber Security', 'New Blacklisted webpage added!', f"You successfuly added a new Blacklisted website! ({FORRBIDEN_WEBPAGE})", r"\images/system_scan_fine.ico", 'False', '', '')
        else:
            print(f"{EMPTUM_CONSOLE_PREFIX}The Webpage's name is incorrect! ")
    
    def clearwebcache(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.isTokenLatest()
        print(f'{EMPTUM_CONSOLE_PREFIX}Clearing the cache of Blacklisted websites!')
        os.system(r'host_settings_clearcache.bat')

    def mixscansettings(self):
        mixed = ''
        if self.wallpapertoogle == True: mixed = mixed + 'scan.wallpaper.wallon\n'
        elif self.wallpapertoogle == False: mixed = mixed + 'scan.wallpaper.walloff\n'
        if self.installationstoogle == True: mixed = mixed + 'scan.installs.installson\n'
        elif self.installationstoogle == False: mixed = mixed + 'scan.installs.installsoff\n'
        if self.startuptoogle == True: mixed = mixed + 'scan.startup.starton\n'
        elif self.startuptoogle == False: mixed = mixed + 'scan.startup.startoff\n'
        if self.runtimetoogle == True: mixed = mixed + 'scan.runtime.runtimeon'
        elif self.runtimetoogle == False: mixed = mixed + 'scan.runtime.runtimeoff'

        with open(r'scansettings.sv', 'w') as f:
            f.close()
            pass
        with open(r'scansettings.sv', 'a') as f:
            f.write(mixed)

    def injectInstallations(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
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
        sound_thread = clickSoundThread()
        sound_thread.start()
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
        
    def installationscheck(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.isTokenLatest()
        installation_found = False
        
        for app in self.INSTALLATIONS_INJECTS:
            for item in winapps.list_installed():
                if item.name.lower().__contains__(app.lower()):
                    installations.append(item.name)
                    found = found + f'{EMPTUM_CONSOLE_PREFIX} {item.name} found, installed at: {item.install_date}!\n'
                    print(f'{EMPTUM_CONSOLE_PREFIX} {item.name} found, installed at: {item.install_date}!\n')
                    with open('installations.hs', 'a', encoding='utf-8') as f:
                        toastNotification('SENTRY - Better School Cyber Security', f'Installation found! - {current_date}', "SENTRY detected Blacklisted installation in your system! Action reported, and logged!", r"\images/system_alert.ico", 'False', '', '')
                        
                        f.write(found)
                        f.close()
                        installation_found = True
        
        if installation_found:
            print(f'{EMPTUM_CONSOLE_PREFIX}Blacklisted installations found and logged!')
            installation_found = False

    def EXPERTSCANLOAD(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        self.expertscan_frame.grid_forget()
        self.scanning_frame.grid(row=0, column=0, sticky="nsew", padx=100)
        self.scantext = customtkinter.CTkLabel(self.scanning_frame, text=f"Scanning installations, desktop, downloads, \nstartup, and runtime as {self.USERNAME_INPUT} \nat {current_date} {current_time}. \nClick on the button to start!",
                                            font=customtkinter.CTkFont(size=10))
        self.scantext.grid(row=6, column=0, padx=15, pady=(20, 0))
    
    
    def EXPERTSCAN(self):
        sound_thread = clickSoundThread()
        sound_thread.start()
        RUNTIME_PROCESSES = []
        noBlacklistedActivity = True 
        global MACHINE_ID
        global APPLICATION_KEYS_LOADED

        self.scantext = customtkinter.CTkLabel(self.scanning_frame, text=f"Scanning installations, desktop, downloads, \nstartup, and runtime as {self.USERNAME_INPUT} \nat {current_date} {current_time}. \nScan finished!",
                                            font=customtkinter.CTkFont(size=10))
        self.scantext.grid(row=6, column=0, padx=15, pady=(20, 0))
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, str(CWD_PATH) + r"\images\sentry_default_wallpaper.png" , 0) 
        
        self.injectInstallations()
        self.injectApplications()

        for process in psutil.process_iter():
            process_name = process.name()
            RUNTIME_PROCESSES.append(process_name)
            
            for app_name in self.APPLICATION_INJECTS:
                if app_name["app"] == process_name:
                    reportToSQLDatabase(f'[!][RUNTIME][{app_name["app"]}]', f'{current_date} {current_time}', MACHINE_ID, 'Blacklisted application in runtime!')
                    
                    with open('activity_log.hs', 'a', encoding='utf-8') as hs:
                        hs.write(f'[Activity]> Forbidden application in the system: {app_name["app"]} at {raw_datetime()}!\n')
                        hs.close()
                    
                    noBlacklistedActivity = False
                    print(EMPTUM_CONSOLE_PREFIX + "A Blacklisted process was found!")
                    os.system("taskkill /f /im " + '"' + app_name["app"] + '"')
                    print(EMPTUM_CONSOLE_PREFIX + "Process has been terminated!")
                    toastNotification('SENTRY - Better School Cyber Security', f"Blacklisted activity! - {current_date}", 'SENTRY detected Blacklisted activity in your runtime! Action reported, and logged!', r"\images/system_alert.ico", 'False', '', '')
                    self.APPLICATION_INJECTS = []
        
        installation_found = any(
            item.name.lower().__contains__(installed_app["app"].lower())
            for installed_app in self.INSTALLATIONS_INJECTS
            for item in winapps.list_installed()
        )
        
        if installation_found:
            with open(r'reports.txt', 'a') as f:
                f.write(f'Application;{current_date}{current_time};Blacklisted installation\n')
        
            noBlacklistedActivity = False
            toastNotification('SENTRY - Better School Cyber Security', f"Blacklisted installation! - {current_date}", 'SENTRY detected Blacklisted installation in your system! Action reported, and logged!', r"\images/system_alert.ico", 'False', '', '')
            reportToSQLDatabase(f'[!][INSTALLATION]', f'{current_date} {current_time}', MACHINE_ID, 'Blacklisted installation found!')
        if noBlacklistedActivity:
            toastNotification('SENTRY - Better School Cyber Security', f"No Blacklisted activity! - {current_date}", 'There is no Blacklisted activity in your system!', r"\images/system_scan_fine.ico", 'False', '', '')
            with open('activity_log.hs', 'a', encoding='utf-8') as hs:
                hs.write(f'[Activity]> No forbidden application found at {raw_datetime()}!\n')
                hs.close()
        
        path = f'C://Users//{os.getenv("USERNAME")}//AppData//Roaming//Microsoft//Windows//Start Menu//Programs//Startup//'
        ss_list = os.listdir(path)
        illegalFileInStartup = False

        print(f'{EMPTUM_CONSOLE_PREFIX}Found files in startup folder: {Fore.MAGENTA}{ss_list}')
        for file in ss_list:
            if 'desktop.ini' in file: pass
            else:
                print(f'{EMPTUM_CONSOLE_PREFIX}{Fore.YELLOW}{file} found, deleted!') 
                illegalFileInStartup = True
                os.remove(path + file)
                with open(r'reports.txt', 'a') as f:
                    f.write(f'{file};{current_date}{current_time};Blacklisted file in startup\n')
                        
        if illegalFileInStartup != True: print(f'{EMPTUM_CONSOLE_PREFIX}No illegal file(s) found in Startup folder!')


if __name__ == "__main__":
    time.sleep(6)
    app = App()
    app.mainloop()
