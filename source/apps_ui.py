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
reports = []

if os.path.isfile(r"reports.txt"):
    pass
else:
    with open(r"reports.txt", 'x') as f:
        f.write("")

def read_runtimereports(path):
    f=open(path,encoding="utf-8")
    runtimereport_raw = []
    for x in f:
        dat=x.split(";")
        d={}
        d["appname"]=str(dat[0])
        d["appdate"]=str(dat[1])
        runtimereport_raw.append(d)
    f.close()
    return runtimereport_raw

reports=read_runtimereports(f"{current_path}/unloaded_processes.hs")
reports_string = ''

for index in reports:
    reports_string = reports_string + f"{index['appname']}   --/--   {index['appdate']}\n"
print(reports_string)

class UI(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.login_frame = customtkinter.CTkFrame(self, bg_color= "black")
        self.login_frame.grid(row=0)
        login_image = ImageTk.PhotoImage(Image.open(current_path + r"/images/apps.png"))
        self.fake_button_image = customtkinter.CTkButton(self.login_frame, text="", image = login_image, width=20, height=20, fg_color="#883cdc", hover_color="#883cdc")
        self.fake_button_image .grid(row=0, column=0, padx=15, pady=(10, 0))
        
        self.banner = customtkinter.CTkLabel(self.login_frame, text="Applications loaded;\nAll listed application is blocked.",
                                                 font=customtkinter.CTkFont(size=10))
        self.banner.grid(row=1, column=0, padx=15, pady=(9, 0))
        
        self.information = customtkinter.CTkLabel(self.login_frame, text=f"{current_date} - {current_path}",
                                                 font=customtkinter.CTkFont(size=10))
        self.information.grid(row=2, column=0, padx=15, pady=(0, 1))

        self.information_tags = customtkinter.CTkLabel(self.login_frame, text="[name]                       [date]                       [comment]",
                                                 font=customtkinter.CTkFont(size=12))
        self.information_tags.grid(row=3, column=0, padx=15, pady=(0, 2))

        self.loaded_reports = customtkinter.CTkLabel(self.login_frame, text=f"{reports_string}",
                                                 font=customtkinter.CTkFont(size=12))
        self.loaded_reports.grid(row=4, column=0, padx=15, pady=(0, 0))


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.login_frame = UI(master=self, width=320, height=200)
        self.login_frame.grid(row=0, column=0, padx=20, pady=20)
        self.title("SENTRY - Blacklisted Applications")
        self.resizable(False, False)


app = App()
app.mainloop()