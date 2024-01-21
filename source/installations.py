import os
import time
import datetime
from PIL import Image, ImageTk
import customtkinter

raw_datetime = datetime.datetime.now()
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
local_time = time.localtime()
current_time = time.strftime("%H:%M:%S", local_time)
current_date = datetime.date.today()
current_path = os.path.dirname(os.path.realpath(__file__))

APPLICATION_KEYS_LOADED = []
hs = open('installations.hs', encoding='utf-8')
for x in hs:
    d = {}
    data = x.strip().split(";")
    d["app"]=str(data[0])
    d["datetime"]=str(data[1])
    APPLICATION_KEYS_LOADED.append(d)
hs.close()

apps = ''
for index in APPLICATION_KEYS_LOADED:
    apps = f'{apps}{index["app"]}  --//--  {index["datetime"]}\n'
class UI(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        global APPLICATION_KEYS_LOADED

        self.login_frame = customtkinter.CTkFrame(self, bg_color= "black")
        self.login_frame.grid(row=0)
        login_image = ImageTk.PhotoImage(Image.open(current_path + r"/images/installations_ui.png"))
        self.fake_button_image = customtkinter.CTkButton(self.login_frame, text="", image = login_image, width=20, height=20, fg_color="#883cdc", hover_color="#883cdc")
        self.fake_button_image .grid(row=0, column=0, padx=15, pady=(10, 0))
        
        self.banner = customtkinter.CTkLabel(self.login_frame, text="Blocked Installations loaded;\nAll listed installations are currently being blocked.",
                                                 font=customtkinter.CTkFont(size=10))
        self.banner.grid(row=1, column=0, padx=15, pady=(9, 0))
        
        self.information = customtkinter.CTkLabel(self.login_frame, text=f"{current_date} - {current_path}",
                                                 font=customtkinter.CTkFont(size=10))
        self.information.grid(row=2, column=0, padx=15, pady=(0, 1))

        self.information_tags = customtkinter.CTkLabel(self.login_frame, text="[name]             [date] ",
                                                 font=customtkinter.CTkFont(size=12))
        self.information_tags.grid(row=3, column=0, padx=15, pady=(0, 2))
        self.loaded_reports = customtkinter.CTkLabel(self.login_frame, text=f"{apps}",
                                                 font=customtkinter.CTkFont(size=12))
        self.loaded_reports.grid(row=4, column=0, padx=15, pady=(0, 0))

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.login_frame = UI(master=self, width=370, height=200)
        self.login_frame.grid(row=0, column=0, padx=0, pady=0)
        self.title("SENTRY - Blacklisted Installations")
        self.iconpath = ImageTk.PhotoImage(file=os.path.join("images","runtime_icon.png"))
        self.wm_iconbitmap()
        self.iconphoto(False, self.iconpath)
        self.resizable(False, False)

app = App()
app.mainloop()